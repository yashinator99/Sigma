class User:
    def __init__(self, info_id: int, user_id: int, first_name: str, last_name: str, email: str):
        self.info_id = info_id
        self.user_id = user_id
        self.first_name = first_name
        self.last_name = last_name
        self.email = email

    def __repr__(self) -> str:
        return f"User Info: {self.info_id} + {self.user_id} + {self.first_name} + {self.last_name} + {self.email}"

    def validate_user_info(self) -> bool:
        if len(self.first_name)  < 2 or len(self.last_name) < 2 or len(self.email) < 5:
            return False
        elif len(self.first_name) > 30 or len(self.last_name) > 30 or len(self.email) > 50:
            return False
        else:
            return True