try:
    from flask import Flask
    from flask_sqlalchemy import SQLAlchemy
    from flask_migrate import Migrate
    import os
except ImportError as e:
    print(e)

app=Flask(__name__)
app.config.from_object(os.environ['APP_SETTINGS'])
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=False

db=SQLAlchemy(app)
migrate=Migrate(app, db)

# Do not move this import statement higher up; it will produce circular dependancy errors!
import routes