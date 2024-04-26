from flask import Blueprint, render_template, request, redirect, url_for, session, jsonify
from sqlalchemy import or_
from application.adclick.initiate_ad_click import execute
from application.models.models import Job
jobRoutes = Blueprint('job',__name__)
from application import db
from datetime import datetime
from application.adclick.login import initiate_driver


@jobRoutes.route('/', methods=['GET'])
def home():
    pass


@jobRoutes.route('/add_job', methods=['POST'])
def add_job():
    data = request.form
    user_id = session['id']
    is_random = False
    username = data['username']
    email = data['email']
    password = data['password']
    keywords = data['keywords']
    website = data['clickable_domain']
    number_of_runs = data['number_of_runs']
    time_to_be_executed = datetime.strptime(data['time'], '%H:%M')

    
    try:
        new_job = Job(username=username, email=email, password=password,user_id=user_id, is_random=is_random, keywords=keywords,
                    website=website, number_of_runs=number_of_runs,
                    time_to_be_executed=time_to_be_executed)
        db.session.add(new_job)
        db.session.commit()
        print('job created')
    except Exception as e:
        print(e)
    finally:
        return redirect(url_for('home.index'))
    

@jobRoutes.route('/initiate_job/<int:job_id>', methods=['GET'])
def initiate_job(job_id):
    print('job id', job_id)
    job = Job.query.filter_by(id=job_id).first()
    if initiate_driver(job):
        execute(job)
        
    return jsonify({'message': 'working'})


@jobRoutes.route('/initiate_job_cron/', methods=['GET'])
def initiate_job_cron():
    job = Job.query.filter().first()
    execute(job)
    return jsonify({'message': 'working'})
