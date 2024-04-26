from flask import Flask, render_template, request, redirect, url_for, session
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
app = Flask(__name__)
app.secret_key = 'your_secret_key'

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
db = SQLAlchemy(app)
from application.models.models import User, Job
# db.init_app(app)
Migrate(app, db)



from application.routes.auth_routes import authRoutes
from application.routes.home_routes import homeRoutes
from application.routes.job_routes import jobRoutes

app.register_blueprint(authRoutes)
app.register_blueprint(homeRoutes)
app.register_blueprint(jobRoutes)