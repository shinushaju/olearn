from flask import Flask
from flask.scaffold import F
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
app = Flask(__name__)

#initializing SQLAlchemy
db = SQLAlchemy()

app.config['SECRET_KEY'] = '28e1ff6a5cf7255041c3f6917e2b9b98ffc41e107037e6a29b097f72a3f3856f'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)

#  MODELS
#  ------
from app.models.faculty import Faculty
from app.models.courses import Course


# faculty login manager
faculty_login_manager = LoginManager()
faculty_login_manager.login_view = 'faculty_login'
faculty_login_manager.login_message = "Please login to continue!"
faculty_login_manager.login_message_category = "warning"
faculty_login_manager.init_app(app)

@faculty_login_manager.user_loader
def load_user(user_id):
    # since the user_id is just the primary key of our user table, use it in the query for the user
    return Faculty.query.get(int(user_id))

# VIEWS
# ------
# import main views here
from app.views import main
# import student views here
from app.views.student import auth, main
# import faculty views here
from app.views.faculty import auth, main, course
# import course views here
from app.views.course import routes

with app.app_context():
    db.create_all()
    #db.drop_all()
    print("All Tables", db.engine.table_names())
  