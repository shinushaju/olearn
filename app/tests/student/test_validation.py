from app.utils.student.validate_email import validate_email
from app.utils.student.validate_password import validate_password
from app.utils.student.validate_phone import validate_phone



def test_validate_email():
    assert validate_email("anirudh@tcs.com") == True
    assert validate_email("anirudh.sasi@tcs.") == False
    assert validate_email("anirudh.sasi@tcs.com") == True
    assert validate_email("anirudh.sa#si@tcs.com") == False
    assert validate_email("anirudh60.sasi60@tcs.com") == True
    assert validate_email("anirudh.sasitcs.com") == False
    
    
def test_validate_phone():
    assert validate_phone("+91-9605475907") == True
    assert validate_phone("+1-9605475907") == True
    assert validate_phone("+542-9605475907") == True
    assert validate_phone("+9189-9605475907") == False
    assert validate_phone("+91 9605475907") == True
    assert validate_phone("91 9605475907") == True
    assert validate_phone("+91-96054759077") == False
    assert validate_phone("+91-960547590") == False
    assert validate_phone("+91 960 547 5907") == True
    assert validate_phone("+91 9605 47 5907") == False
    assert validate_phone("+91 960-547-5907") == True
    assert validate_phone("9605475907") == False
    assert validate_phone("+91-(960) 547 5907") == True


def test_validate_password():
    assert validate_password("Anu@3#4") == False
    assert validate_password("0AbcA@13") == False
    assert validate_password("abcdef@1234") == False
    assert validate_password("abcdesd@#!") == False
    assert validate_password("  abc  de") == False
    assert validate_password("AnuA@1489#") == True