import re

def validate_email(email):
    #print(email)
    regex ='^[A-Za-z0-9]+[A-Za-z0-9.$*]+[A-Za-z0-9]+@[A-Za-z]+.com$'
    if(re.fullmatch(regex, email)):
        return True      
    else:
        return False
        

def validate_name(name):
    #print(name)
    regex_name=re.compile('^([A-Za-z]{3,24})+[ A-Za-z]{3,24}$')
    res = regex_name.search(name)
    if res:
        return True
    else:       
        return False

def validate_password(password):
    l, u, p, d = 0, 0, 0, 0
    if (len(password) >= 8 and len(password)<=15):
        for i in password:
            if (i.islower()):
                l+=1                 
            if (i.isupper()):
                u+=1                   
            if (i.isdigit()):
                d+=1            
            if(i=='@'or i=='$' or i=='_' or i=='#'):
                 p+=1  
    if (l>=1 and u>=1 and p>=1 and d>=1 and l+p+u+d==len(password)):  
        return True
    else:    
        return False

        
