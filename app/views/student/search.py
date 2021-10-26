from flask import render_template, request
from flask_login import login_required, current_user

from app import app
from app.models.courses import Course

@login_required
@app.route('/student/search')
def search():
    # Collecting GET parameters
    q=request.args.get('q')
    # searchFilter=request.args.get('filter')
    duration=request.args.get('duration')

    # Note: All searches are case-insensitive

    # Search by course name
    results=Course.query.filter(Course.course_name.ilike('%'+"%".join(q.split(" "))+'%')).all()
    # Filter by course duration
    if (duration is not None) and (duration!='any'):
        results=Course.query.filter(Course.course_name.ilike('%'+"%".join(q.split(" "))+'%') & (Course.course_duration<=int(duration))).all()

    return render_template('student/search.html', courses=results, user=current_user)
