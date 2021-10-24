from app.utils.auth import validate_email,validate_name,validate_password

def test_validate_email():
    assert validate_email("sam13p@tcs.com")==True
    assert validate_email("sptcs.com")==False
    assert validate_email("sptcs@")==False

def test_validate_name():
    assert validate_name("Shinu Shaju")==True
    assert validate_name("ShinuShaju")==True
    assert validate_name("pa")==False
    assert validate_name("pa sa")==False

def test_validate_password():
    assert validate_password("Devops@23")==True
    assert validate_password("Devops#23")==True
    assert validate_password("12356")==False
    assert validate_password("sasg")==False
    assert validate_password("#$")==False
    assert validate_password("Devops@12345678910123")==False


    