# DTO = Data Transfer Object (Representation of going from one to another)

class Register:
    def __init__(self, info_id: int, user_id: int, first_name, last_name):
        self.inf0_id = info_id
        self.user_id = user_id
        self.first_name = first_name
        self.last_name = last_name
        


    def __repr__(self) -> str:
        return f"User Info: id - {self.info-id} + {self.user_id} + {self.first_name} + {self.last_name}"


    def validate_user_info(self) -> bool:
        if len(self.first_name) < 5 or len(self.last_name) < 5:
            return False
        elif len(self.first_name) > 20 or len(self.last_name) > 20:
            return False
        else:
            return True