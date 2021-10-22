from flask import render_template
from app import app

@app.route('/student/dashboard')
def student_dashboard():
    return render_template('student/dashboard.html')