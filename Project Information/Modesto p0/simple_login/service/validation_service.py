from operator import truediv
import re


def validate_login(new_login: tuple) -> bool:
    return validate_username(new_login[0]) and validate_password(new_login[1])


def validate_info(new_info: tuple) -> bool:
    return validate_first_name(new_info[0]) and validate_last_name(new_info[1]) 

def validate_first_name(first_name):
    if re.findall('[A-Za-z]{2,15}', first_name) and len(first_name) <= 15 and not " " in first_name:
        return True
    else:
        return False  
def validate_last_name(last_name):
    if re.findall('[A-Za-z]{2,15}', last_name) and len(last_name) <= 15 and not " " in last_name:
        return True
    else:
        return False  

def validate_username(username):
    if re.findall('[A-Za-z]{2,15}', username) and len(username) <= 15 and not " " in username:
        return True
    else:
        return False  

def validate_password(password):
    if re.findall('[A-Za-z]{2,15}', password) and len(password) <= 15 and not " " in password:
        return True
    else:
        return False  
    