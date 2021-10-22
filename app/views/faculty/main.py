from flask import render_template
from app import app
from flask_login import login_required, current_user

@app.route('/faculty/dashboard')
@login_required
def faculty_dashboard():
    return render_template('faculty/dashboard.html', user=current_user)
