import re

def valid_username(username):
    """
    username 
    1. between 5 to 14 characters
    2. can't start with an underscore
    3. allowed characters are Uppercase, Lowercase, Digits and Underscores
    """
    
    pattern = r'[A-Za-z0-9]{1}[A-Za-z0-9_]{4,14}'
    if re.fullmatch(pattern, username):
        return True
    return False

def valid_password(password):
    """
    password
    1. between 8 to 15 characters
    2. must contain at least 1 Uppercase, 1 Lowercase, 1 digit, and 1 special character (@$!%*?&)
    """
    pattern = r'(?=.*[A-Z])(?=.*[a-z])(?=.*[0-9])(?=.*[@$!%*?&])[A-Za-z0-9@$!%*?&]{8,15}'
    if re.fullmatch(pattern, password):
        return True
    return False

print(valid_username("asdfjkl"))
print(valid_password("Qw1@awsd"))