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

# Class Models
# ------------
from app.models.user import User
from app.models.faculty import Faculty
from app.models.student import Student
from app.models.courses import Course, Section, Lecture
from app.models.discussions import Query, Reply

# login manager configuration
# ------------------------------------
login_manager = LoginManager()
login_manager.login_view = 'login'
login_manager.login_message = "Please login to continue!"
login_manager.login_message_category = "warning"
login_manager.init_app(app)
@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))
    
# View Functions
# ------
# import main views here
from app.views import routes
# import faculty views here
from app.views.faculty import auth, main, course
# import student views here
from app.views.student import auth, routes, createDummyCourses, manage_profile, search, student_review, course, markSectionAsComplete
# import course views here
from app.views.course import routes

# registering jinja2 template filter
# ----------------------------------
from app.utils.format_datetime import format_datetime
from jinja2 import filters
filters.FILTERS['format_datetime']=format_datetime

# app context
# -----------
with app.app_context():
    
    ### commands to drop 
    #User.__table__.drop(db.engine)
    #Faculty.__table__.drop(db.engine)
    #Course.__table__.drop(db.engine)
    #Section.__table__.drop(db.engine)
    #Lecture.__table__.drop(db.engine)
    # Query.__table__.drop(db.engine)
    # Reply.__table__.drop(db.engine)

    db.create_all()
    #db.drop_all()

    print("All Tables", db.engine.table_names())

    ### display all table data
    '''
    print("Database Tables Data")
    print("--------------------")
    print("Users", User.query.all())
    print("Faculties", Faculty.query.all())
    print("Courses", Course.query.all())
    print("Sections", Section.query.all())
    print("Lectures", Lecture.query.all())
    '''