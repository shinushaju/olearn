from flask import render_template, request, redirect, url_for
from flask_login import login_required, current_user

from app import app
from app.models.courses import Course

@login_required
@app.route('/search/results')
def search():
    # Collecting GET parameters
    q=''
    duration=''
    if request.args.get('q'):
        q=request.args.get('q').strip()
    # searchFilter=request.args.get('filter')
    if request.args.get('duration'):
        duration=request.args.get('duration').strip()

    # Note: All searches are case-insensitive

    # Search by course name
    if request.args.get('q'):
        results=Course.query.filter(Course.course_name.ilike('%'+"%".join(q.split(" "))+'%')).all()
    # Filter by course duration
    if duration and (duration!='any') and q:
        results=Course.query.filter(Course.course_name.ilike('%'+"%".join(q.split(" "))+'%') & (Course.course_duration<=int(duration))).all()
    if not q:
        if current_user.is_faculty():
            return redirect(url_for('faculty_dashboard'))
        if current_user.is_student():
            return redirect(url_for('student_dashboard'))
    return render_template('search.html', courses=results, user=current_user)
