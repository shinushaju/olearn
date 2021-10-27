from flask import render_template
from flask_login import login_required, current_user
from app import app

@app.route('/student/student_explore')
@login_required
def student_explore():
    return render_template('/student/student_explore.html',user=current_user)

