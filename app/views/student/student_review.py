from flask import Flask, request, flash, url_for, redirect, render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE-URI'] = 'sqlite:///db.sqlite'
app.config['SECRET_KEY'] ="random string"

db=SQLAlchemy(app)

class review(db.Model):
    id=db.Column('student_id',db.Integer,primary_key=True)
    subject=db.Column(db.String(100), nullable=False)
    rating=db.Column(db.Integer, nullable=False)

    def __init__(self,subject,rating):
        self.subject=subject
        self.rating=rating
    
db.create_all()
db.session.commit()

@app.route('/student/student_review', methods = ['GET','POST'])
def student_review():
    if request.method == 'POST':
        if not request.form['subject'] or not request.form['rating'] :
            flash("Please enter all the fields",'error')
        else:
            subject=request.form['subject']
            rating=request.form['rating']
            r1 = review(subject=subject,rating=rating)
            db.session.add(r1)
            db.session.commit()
           
            return render_template('/student/student_review.html')
    return render_template('/student/student_review.html')

@app.route('/student/show_review')
def show_review():
    print(review.query.all())
    return render_template('/student/show_review.html',review=review.query.all())

if __name__ == '__main__' :
    app.run(debug = True)
       
