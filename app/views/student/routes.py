from flask import render_template
from flask_login import login_required, current_user
from app import app

@app.route('/student/dashboard')
@login_required
def student_dashboard():
    return render_template('student/dashboard.html', user=current_user)

