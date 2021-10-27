import re

def validate_email(email):
    #print(email)
    regex ='^(?!\.)(?!.*\.$)(?!.*\.@)(?!.*_@)(?!\d)(?!_)(?!.*?\.\.)(?!.*?\_\_)(?!.*?\._)(?!.*?_\.)(?!-)(?!.*-@)(?!.*?\-\-)(?!.*?\.-)(?!.*?-\.)(?!.*?-_)(?!.*?_-)([A-Za-z0-9._-]{3,})+@[A-Za-z]+\.[a-z]{2,}$'

    if(re.fullmatch(regex, email)):
        #print("valid email")
        return True      
    else:
        #print("invalid email")
        return False
        

def validate_name(name):
    #print(name)
    if(len(name)>=3 and len(name)<=30):
        regex_name=re.compile('^([a-z]+)( [a-z]+)*( [a-z]+)*$', re.IGNORECASE)
        if(re.fullmatch(regex_name, name)):
            #print("valid name")
            return True
        else:
            #print("invalid name")
            return False
    return False

def validate_password(password):
    #print(password)
    regex_password=re.compile(r'^(?!\_)(?!\#)(?!\$)(?!\@)(?!\d)(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@_$#])[A-Za-z\d@$_#]{8,19}$')
    if(re.fullmatch(regex_password, password)):
        #print("valid password")
        return True
    else:
        #print("invalid password")
        return False

        
