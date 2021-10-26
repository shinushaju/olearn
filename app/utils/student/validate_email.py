import re

regex ='^(?!\.)(?!.*\.$)(?!.*?\.\.)[A-Za-z0-9]+[A-Za-z0-9.]+[A-Za-z0-9]+@[A-Za-z]+\.[a-z]{2,}$'
 
def validate_email(email):
    if(re.fullmatch(regex, email)):
        return True
    else:
        return False