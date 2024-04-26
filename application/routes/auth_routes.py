from flask import Blueprint, render_template, request, redirect, url_for, session, jsonify
from sqlalchemy import or_
from application.models.models import User, create_user
authRoutes = Blueprint('auth',__name__)



@authRoutes.route('/register', methods=['GET'])
def register():
    # data = request.get_json()
    username = 'username'
    email = 'email@email.com'
    password = 'password'

    if not username or not email or not password:
        return jsonify({'error': 'Please provide username, email, and password'}), 400

    if (User.query.filter_by(email=email).first()):
        return jsonify({'error': 'Email already registered'}), 400
    
    if not create_user(username, email, password):
         return jsonify({'message': 'Error while registering. Please try again'}), 201
     
    return jsonify({'message': 'User registered successfully'}), 201

@authRoutes.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        user = User.query.filter_by(email=email).first()
        if user and user.check_password(password):
            session['id'] = user.id
            print('logged in')
            return redirect(url_for('home.index'))
        else:
            return render_template("pages/login.html", error='Invalid username or password')
    return render_template("pages/login.html", error=None)


@authRoutes.route('/logout')
def logout():
    session.pop('id', None)
    return redirect(url_for('auth.login'))