from functools import wraps
from flask import url_for, redirect
from app.models.student import Student
from flask_login import current_user

### decorator function to restrict view access to student only
def student_role_required(*args):
    def decorator(access):
        @wraps(access)
        def decorated_function(*args, **kwargs):
            student = current_user
            if student and not student.is_student():
                return redirect(url_for('student_login'))
            return access(*args, **kwargs)
        return decorated_function
    return decorator