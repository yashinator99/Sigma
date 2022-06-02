# Data Transfer Object

import re

class Login:
    def __init__(self, user_id, username, password):
        self.user_id = user_id
        self.username = username
        self.password = password

    def __repr__(self) -> str:
        return f"User Login: id - {self.user_id} username - {self.username} password - {self.password}"

    def validate_login(username: str, password: str) -> bool:
        """
        username 
        1. between 5 to 14 characters
        2. can't start with an underscore
        3. allowed characters are Uppercase, Lowercase, Digits and Underscores
        """
        user_pattern = r'[A-Za-z0-9]{1}[A-Za-z0-9_]{4,14}'

        """
        password
        1. between 8 to 15 characters
        2. must contain at least 1 Uppercase, 1 Lowercase, 1 digit, and 1 special character (@$!%*?&)
        """
        password_pattern = r'(?=.*[A-Z])(?=.*[a-z])(?=.*[0-9])(?=.*[@$!%*?&])[A-Za-z0-9@$!%*?&]{8,15}'
        
        if re.fullmatch(user_pattern, username) and re.fullmatch(password_pattern, password):
            return True
        return False