from flask import Flask, request, flash, url_for, redirect, render_template
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash
### importing regex library from base python itself
import re

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///students.sqlite3'
app.config['SECRET_KEY'] = "random string"

db = SQLAlchemy(app)


class students(db.Model):
   id = db.Column('student_id', db.Integer, primary_key = True)
   #roll_Number = db.Column(db.String(50),primary_key = True)
   email_Id = db.Column(db.String(50),unique=True, nullable=False)
   password = db.Column(db.String(10), nullable=False) 
   
   
   def __init__(self, email_Id,password):
      self.email_Id =email_Id
      #self.password = generate_password_hash(password)
      self.password = password

## Need to add these two lines to craete the table initially 
db.create_all()
db.session.commit()
#### Very dangerous comment as it will drop all the tables from the database ######################
###db.drop_all()
###db.session.commit()
#### Very dangerous comment as it will drop all the tables from the database ######################


@app.route('/register', methods = ['GET', 'POST'])
def register():
   if request.method == 'POST':
      if not request.form['email_Id'] or not request.form['password'] :
         flash('Please enter all the fields', 'error')
      else:
         email_Id = request.form['email_Id']
         password = request.form['password']
         data = students.query.filter_by(email_Id=email_Id).first()
         if data is None:
            ## It is a strange syntax to initialize the fields
            s1 = students(email_Id=email_Id,password=password)
            db.session.add(s1)
            db.session.commit()
            flash('Record was successfully added')
            return render_template('show_all.html')
         else:
            flash('Email Id already exists!!!!')
            flash('Please use the correct password to log in!!!!')
            render_template('register.html')
   return render_template('register.html')

@app.route('/show_all')
def show_all():
   print(students.query.all())
   return render_template('show_all.html', students = students.query.all() )

##### Code deletes a particular record ####

@app.route('/delete_one/<id>')
def delete_one(id):
   data = students.query.get(id)
   print("", vars(data))
   ### deletes the student with the given id
   if data:
      db.session.delete(data)
      db.session.commit()
   #print(students.query.all())
   flash("Selected student is successfully deleted from the database!!!!")
   return render_template('show_all.html', students = students.query.all() )

@app.route('/edit_one/<id>' , methods = ['GET', 'POST'])
def edit_one(id):
   if request.method == 'POST':
      if not request.form['email_Id']:
         ### add validation for the email Id - gowthami
         flash('Please enter proper email Id', 'error')
      else:
         email_Id = request.form['email_Id']
         student = students.query.get(id)
         
         if student :
            data = students.query.filter_by(email_Id=email_Id).first()

            if data is None:
               student.email_Id = email_Id
               db.session.commit()
               flash('Record is successfully updated')
               return redirect(url_for("show_all"))
            else:
               flash('Use a different Email ID !!! Email Id is not available for registration!!!!')
              
         else:
            flash('Student does not exist!!!!')
            flash('Please use the correct password to log in!!!!')
            
   return render_template('edit_one.html',result = students.query.get(id))



@app.route('/delete_all')
def delete_all():
   students.query.delete()
   db.session.commit()
   return render_template('delete_all.html', students = students.query.all() )

if __name__ == '__main__':
#   db.create_all()
   app.run(debug = True)