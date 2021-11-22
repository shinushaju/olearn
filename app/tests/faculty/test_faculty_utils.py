
from app.utils.faculty.course import validate_course_name,validate_course_overview,validate_course_preview_link,validate_course_duration,validate_course_price,validate_section_title,validate_section_outcome,validate_lecture_title,validate_lecture_link,validate_lecture_duration

def test_validate_course_name():
    assert validate_course_name("R programming")==True
    assert validate_course_name("HTML5 and CSS")==True
    assert validate_course_name("R.programming")==False
    assert validate_course_name("123")==False

def test_validate_course_overview():
    assert validate_course_overview("Data science is the field of study that combines domain expertise, programming skills, and knowledge of mathematics and statistics to extract meaningful insights from data.")==True
    assert validate_course_overview("123Datascience")==False
    assert validate_course_overview("Block Chain 12334 %432 :{} Technology.")==True

def test_validate_course_preview_link():
    assert validate_course_preview_link("https://youtu.be/TngLevtn45c")==True
    assert validate_course_preview_link("https://www.youtube.com/watch?v=fnqCSQ3WGTw")==True
    assert validate_course_preview_link("")==False
    

def test_validate_course_duration():
    assert validate_course_duration("7")==True
    assert validate_course_duration("abc")==False
    assert validate_course_duration("@12")==False

def test_validate_course_price():
    assert validate_course_price("500.00")==True
    assert validate_course_price("abc")==False
    assert validate_course_price("125")==False
   
def test_validate_section_title():
    assert validate_section_title("Basics to Python")==True
    assert validate_section_title("Introduction to CSS")==True
    assert validate_section_title("12356")==False
    

def test_validate_section_outcome():
    assert validate_section_outcome("scientific thinking")==True
    assert validate_section_outcome("12356")==False
    

def test_validate_lecture_title():
    assert validate_section_title("Basics to Python.")==True
    assert validate_section_title("Introduction to CSS")==True
    assert validate_section_title("12356")==False

def test_validate_lecture_link():
    assert validate_course_preview_link("https://youtu.be/TngLevtn45c")==True
    assert validate_course_preview_link("https://www.youtube.com/watch?v=fnqCSQ3WGTw")==True
    assert validate_course_preview_link("")==False
    
def test_lecture_duration():
    assert validate_course_duration("70")==True
    assert validate_course_duration("abc")==False
    assert validate_course_duration("@12")==False

    

