from datetime import datetime
from enum import unique
from operator import index
import bcrypt
from flask_login import UserMixin
from sqlalchemy import PrimaryKeyConstraint

class User(UserMixin, db.Model):
    __tablename__="users"


    id = db.Column(db.Integer, primary_key=True)
    user_name = db.Column(db.String(60))
    user_email = db.Column(db.String(60), unique=True, index=True)
    user_password = db.Column(db.String(80))
    regristration_date = db.Column(db.DateTime, default=datetime.now)

    #app/auth/models.py

    def check_password(self, password):
        return bcrypt.check_password_hash(self.user_password, password)

    #class method belongs to a class but not associated to any class instance
    @classmethod
    def create_user(cls, user, email, password):

        user = cls(user_name=user,
                   user_email=email,
                   user_password=bcrypt.generate_password_hash(password).decode('utf-8')
                   )

        db.session.add(user)
        db.session.commit()

        return

@login_manager.user_loader
def load_user(id):
    return User.query.get(int(id))