from functools import wraps
from flask import url_for, redirect
from app.models.faculty import Faculty
from flask_login import current_user

### decorator function to restrict view access to faculty only
def faculty_role_required(*args):
    def decorator(access):
        @wraps(access)
        def decorated_function(*args, **kwargs):
            faculty = current_user
            if faculty and not faculty.is_faculty():
                return redirect(url_for('faculty_login'))
            return access(*args, **kwargs)
        return decorated_function
    return decorator
