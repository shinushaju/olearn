from app.utils.auth import validate_email,validate_name,validate_password

def test_validate_email():
    assert validate_email("hon.ey@test.com")==True
    assert validate_email("honey@t.org")==True 
    assert validate_email(" @test.com")==False
    assert validate_email("   ")==False
    assert validate_email("exa..m@test.in")==False
    assert validate_email("ExAM9@yahoo.com")==True
    assert validate_email("ExAM9@gmail@gmail.com")==False
    assert validate_email(".honey13@yahoo.in")==False
    assert validate_email("honey13@yahoo.in.")==False
    assert validate_email("honey13.@yahoo.in")==False
    assert validate_email("")==False
    assert validate_email("samy._kanda@gmail.com")==False
    assert validate_email("samy_.kanda@gmail.com")==False
    assert validate_email("9samykanda@gmail.com")==False
    assert validate_email("samy__kanda@gmail.com")==False
    assert validate_email("samykanda@_gmail.com")==False
    assert validate_email("samykanda_@gmail.com")==False
    assert validate_email("samykanda@gmail._com")==False
    assert validate_email("samykanda@gmail.com_")==False
    assert validate_email("samykanda@gmail.com.com")==False
    assert validate_email("samy-kanda_.@gmail.com")==False
    assert validate_email("samy-_.kanda@gmail.com")==False
    assert validate_email("samy-._@gmail.com")==False
    assert validate_email("samy--kanda@gmail.com")==False
    assert validate_email("samy-kanda.52@gmail.com")==True

def test_validate_name():
    assert validate_name("Shinu Shaju")==True
    assert validate_name("ShinuShaju")==True
    assert validate_name("pa")==False
    assert validate_name("pa  s   a")==False
    assert validate_name("pa")==False
    assert validate_name("   ")==False

def test_validate_password():
    assert validate_password("Aacdefg_7")==True
    assert validate_password("1dhjvhf88")==False
    assert validate_password("adggA_7")==False
    assert validate_password("Abdsssgsyfsbcxgysddsycd89_9")==False
    assert validate_password("_Ahsdfajk89")==False
    assert validate_password("A123abc@")==True
    assert validate_password("s@#$_@#$_$$$")==False
    assert validate_password("9@sdfgh1234")==False
    assert validate_password("ABCDEFGHIJKL")==False
    assert validate_password("abcdefghijkl")==False
    assert validate_password("@@@@__$$___##_$")==False
    assert validate_password("123456789012")==False
    assert validate_password("abcd@9596$")==False
    assert validate_password("adMin_25#05$20D")==True
    assert validate_password("Abc d@9596$")==False
    assert validate_password("1Abcd@9596$")==False
    

    