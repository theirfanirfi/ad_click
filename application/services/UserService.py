from application.models.models import User
from sqlalchemy import or_


class UserService:
    def __init__(self):
        pass
    @staticmethod
    def create_user(username, email, password):
        pass
    @staticmethod
    def query_user_unique(usernameOrEmail):
        return User.query.filter_by(or_(username=usernameOrEmail, email=usernameOrEmail))