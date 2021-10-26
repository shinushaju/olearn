import re

def validate_phone(value):
    rule = re.compile(r'(^\+?\d{0,3}[-\s]?\(?\d{3}\)?[-.\s]?\d{3}[-.\s]?\d{4}$)')
    if rule.search(value):
        return True
    else:
        return False