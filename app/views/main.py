from flask import render_template
from app import app

@app.route('/')
def home():
    return render_template('home/home.html')

@app.route('/about')
def about():
    return render_template('home/about.html')

@app.route('/careers')
def careers():
    return render_template('home/careers.html')

@app.route('/contact')
def contact():
    return render_template('home/contact.html')

@app.route('/courses')
def courses():
    return render_template('home/courses.html')

@app.route('/courses/data-science')
def data_science_course():
    return render_template('home/courses/data-science.html')

@app.route('/courses/programming')
def programming_course():
    return render_template('home/courses/programming.html')

@app.route('/courses/artificial-intelligence')
def artificial_intelligence_course():
    return render_template('home/courses/artificial-intelligence.html')

@app.route('/courses/blockchain')
def blockchain_course():
    return render_template('home/courses/blockchain.html')

@app.route('/courses/cloud-computing')
def cloud_computing_course():
    return render_template('home/courses/cloud-computing.html')

@app.route('/courses/quantum_computing')
def quantum_computing_course():
    return render_template('home/courses/quantum-computing.html')

@app.route('/course-details')
def course_details():
    return render_template('home/course-details.html')

@app.route('/faculty')
def faculty():
    return render_template('home/faculty.html')

@app.route('/programs')
def programs():
    return render_template('home/programs.html')

@app.route('/students')
def students():
    return render_template('home/students.html')

@app.route('/testimonials')
def testimonials():
    return render_template('home/testimonials.html')

# sign-up main screen
@app.route('/sign-up')
def sign_up():
    return render_template('home/sign-up.html')

# login main screen
@app.route('/login')
def login():
    return render_template('home/login.html')

@app.errorhandler(404)
def page_not_found(e):
    # note that we set the 404 status explicitly
    return render_template('home/404.html'), 404