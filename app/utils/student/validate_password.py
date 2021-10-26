import re

regex ="^(?=.*[a-z])(?=.*[A-Z])(?![0-9])(?=.*[@$!%*#?&])[A-Za-z\d@$!_#%*?&]{8,25}$"
 
def validate_password(password):
 
    if(re.fullmatch(regex, password)):
        return True
 
    else:
        return False