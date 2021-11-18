from datetime import datetime
from jinja2 import environment

from app import app

@app.template_filter()
def format_datetime(value, format="date"):
    """Abhiram Santhosh: This utility function takes a datetime.datetime object
    and returns it in a nice, human readable format to be used in an html template.
    Example format outputs
    "date" - 23 Jun, 2021
    "time" - 9:43 AM
    """

    # Setting a format
    if format=="time":
        FORMAT="%-I:%M %p"
    else:
        FORMAT="%d %b, %Y"

    return value.strftime(FORMAT)