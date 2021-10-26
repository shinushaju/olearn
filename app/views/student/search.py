import re
from flask import render_template, request
from flask_login import login_required, current_user

from app import app
from app.models.courses import Course

@login_required
@app.route('/student/search')
def search():
    form=dict()
    # Collecting GET parameters
    form['q']=request.args.get('q')
    # searchFilter=request.args.get('filter')
    form['duration']=request.args.get('duration')

    # Note: All searches are case-insensitive

    # Search by course name
    results=Course.query.filter(Course.course_name.ilike('%'+"%".join(form['q'].split(" "))+'%'))
    # Filter by course duration
    if form['duration'] is not None:
        results=Course.query.filter(Course.course_name.ilike('%'+"%".join(form['q'].split(" "))+'%') & (Course.course_duration<=int(form['duration'])))

    return render_template('student/search.html', courses=results, user=current_user, form=form)
