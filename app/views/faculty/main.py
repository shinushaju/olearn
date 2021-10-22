from flask import render_template
from app import app

@app.route('/faculty/dashboard')
def faculty_dashboard():
    return render_template('faculty/dashboard.html')
