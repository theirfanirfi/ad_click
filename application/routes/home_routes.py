from flask import Blueprint, render_template, request, redirect, url_for, session, jsonify
from sqlalchemy import or_
from application.models.models import User, Job
homeRoutes = Blueprint('home',__name__)



@homeRoutes.route('/', methods=['GET'])
def home():
    if not 'id' in session:
        return redirect(url_for('auth.login'))
    return redirect(url_for("home.index"))


@homeRoutes.route('/index', methods=['GET'])
def index():
    if not 'id' in session:
        return redirect(url_for('auth.login'))
    
    id = session['id']
    jobs = Job.query.filter_by(user_id=id).all()
    return render_template("pages/home.html", jobs=jobs)
