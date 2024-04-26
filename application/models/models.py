from application import db
from werkzeug.security import generate_password_hash, check_password_hash

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(60), nullable=False)
    jobs = db.relationship('Job', backref='user', lazy=True)
    
    def set_password(self, password):
            self.password = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password, password)

    def __repr__(self):
        return f"User('{self.username}', '{self.email}')"

class Job(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(200))
    email = db.Column(db.String(200))
    password = db.Column(db.String(200))
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    is_random = db.Column(db.Boolean, default=False)

    keywords = db.Column(db.String(200))
    website = db.Column(db.String(200))
    number_of_runs = db.Column(db.Integer, default=0)
    time_to_be_executed = db.Column(db.String(50))

    def __repr__(self):
        return f"Job('{self.user.username}', '{self.website}')"
    

def create_user(username, email, password):
    try:
        new_user = User(username=username, email=email)
        new_user.set_password(password)
        print(new_user.password)
        db.session.add(new_user)
        db.session.commit()
        return True
    except Exception as e:
        print(e)
        return False