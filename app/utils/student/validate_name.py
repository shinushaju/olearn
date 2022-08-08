
def validate_name(name):
    if (any(char.isdigit() for char in name)) == True:
        return False
    else:
        return True