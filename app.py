from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def home():
    return render_template('home.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/careers')
def careers():
    return render_template('careers.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/courses')
def courses():
    return render_template('courses.html')

@app.route('/courses/data-science')
def data_science_course():
    return render_template('courses/data-science.html')

@app.route('/courses/programming')
def programming_course():
    return render_template('courses/programming.html')

@app.route('/courses/artificial-intelligence')
def artificial_intelligence_course():
    return render_template('courses/artificial-intelligence.html')

@app.route('/courses/blockchain')
def blockchain_course():
    return render_template('courses/blockchain.html')

@app.route('/courses/cloud-computing')
def cloud_computing_course():
    return render_template('courses/cloud-computing.html')

@app.route('/courses/quantum_computing')
def quantum_computing_course():
    return render_template('courses/quantum-computing.html')

@app.route('/course-details')
def course_details():
    return render_template('course-details.html')

@app.route('/faculty')
def faculty():
    return render_template('faculty.html')

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/programs')
def programs():
    return render_template('programs.html')

@app.route('/sign-up')
def sign_up():
    return render_template('sign-up.html')

@app.route('/students')
def students():
    return render_template('students.html')

@app.route('/testimonials')
def testimonials():
    return render_template('testimonials.html')

@app.route('/submit')
def submit():
    return render_template('submit.html')

@app.route('/students/join')
def student_signup():
    return render_template('student-signup.html')

@app.route('/faculty/join')
def faculty_signup():
    return render_template('faculty-signup.html')
    
if __name__ == '__main__':
    app.run(debug=True)
    