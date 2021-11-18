from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager

app = Flask(__name__)

#initializing SQLAlchemy
db = SQLAlchemy()

app.config['SECRET_KEY'] = '28e1ff6a5cf7255041c3f6917e2b9b98ffc41e107037e6a29b097f72a3f3856f'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)

from app.models.user import User
from app.models.student import Student
from app.models.faculty import Faculty

# Login manager configuration
login_manager = LoginManager()
login_manager.login_view = 'student_login'
login_manager.init_app(app)

@login_manager.user_loader
def load_user(id):
    # since the user_id is just the primary key of our user table, use it in the query for the user
    return User.query.get(int(id))
    
# VIEWS
# ------
# import main views here
from app.views import routes
# import student views here
from app.views.student import auth, routes, createDummyCourses, manage_profile, search, student_review, course, markSectionAsComplete
# import faculty faculty views here
from app.views.faculty import auth, main

from app.utils.format_datetime import format_datetime

from jinja2 import filters
filters.FILTERS['format_datetime']=format_datetime

with app.app_context():
    db.create_all()
  