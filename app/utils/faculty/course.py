import re
def validate_course_name(course_name):
    if(len(course_name)>=1 and len(course_name)<=250):
        regex_name=re.compile('^(?=.*?[A-Za-z])([a-z0-9]+)( [a-z0-9]+)*( [a-z0-9]+)*$', re.IGNORECASE)
        if(re.fullmatch(regex_name,course_name)):
            return True
        else:
            return False
    return False

def validate_course_overview(course_overview):
    if(len(course_overview)>=4 and len(course_overview)<=1000):
        regex_name=re.compile('^(?=.*?[A-Za-z])(?!\.)(?!.*?  )(?!.*?\.\.)(?!.*?\,\,)(.|\s)*[a-zA-Z0-9]+(.|\s)*\.$')
        res = regex_name.search(course_overview)
        if res:
            return True 
        else:   
            return False
    return False

def validate_course_preview_link(preview_link):
    if(len(preview_link)>=3 and len(preview_link)<=150):
        regex_name=re.compile('^(https?\:\/\/)?((www\.)?youtube\.com|youtu\.?be)\/.+$')
        res = regex_name.search(preview_link)
 
        if res:

            return True 
        else: 
        
            return False
    return False

def validate_course_duration(course_duration): 
    regex ='^[0-9]+$'
    if(re.search(regex,course_duration)): 
        return True         
    else: 
        return False

def validate_course_price(course_price): 
    regex ='^[0-9]+\.[0-9]+$'
    if(re.search(regex,course_price)): 
        return True         
    else: 
        return False

def validate_section_title(section_title):
    if(len(section_title)>=1 and len(section_title)<=250):
        regex_name=re.compile('^(?=.*?[A-Za-z])(?!\.)(?!\+)(?!\#)([a-z+.#0-9]+)( [a-z+.#0-9]+)*( [a-z+.#0-9]+)*$', re.IGNORECASE)
        if(re.fullmatch(regex_name,section_title)):
            return True
        else:
            return False
    return False

def validate_section_outcome(section_outcome):
    if(len(section_outcome)>=4 and len(section_outcome)<=250):
        regex_name=re.compile('^(?=.*?[A-Za-z])(?!\.)(?!.*?  )(?!.*?\.\.)(?!.*?\,\,)(.|\s)*[a-zA-Z0-9]+(.|\s)*\.$')
        res = regex_name.search(section_outcome)
        if res:
            return True 
        else:   
            return False
    return False

def validate_lecture_title(lecture_title):
    if(len(lecture_title)>=1 and len(lecture_title)<=250):
        regex_name=re.compile('^(?=.*?[A-Za-z])(?!\.)(?!\+)(?!\#)([a-z+.#0-9]+)( [a-z+.#0-9]+)*( [a-z+.#0-9]+)*$', re.IGNORECASE)
        if(re.fullmatch(regex_name,lecture_title)):
            return True
        else:
            return False
    return False

def validate_lecture_link(lecture_link):
    if(len(lecture_link)>=3 and len(lecture_link)<=150):
        regex_name=re.compile('^(https?\:\/\/)?((www\.)?youtube\.com|youtu\.?be)\/.+$')
        res = regex_name.search(lecture_link)
 
        if res:

            return True 
        else: 
        
            return False
    return False

def validate_lecture_duration(lecture_duration): 
    regex ='^[0-9]+$'
    if(re.search(regex,lecture_duration)): 
        return True         
    else: 
        return False