class User:
    def __init__(self, user_id: int, email: str, first_name: str, last_name: str, phone_number: str, address_1: str, address_2: str, city: str, state: str, country: str, zip_code: str):
        self.user_id = user_id
        self.email = email
        self.first_name = first_name
        self.last_name = last_name
        self.phone_number = phone_number
        self.address_1 = address_1
        self.address_2 = address_2
        self.city = city
        self.state = state
        self.country = country
        self.zip_code = zip_code

    def __repr__(self) -> str:
        return f"user_id - {self.user_id}, {self.first_name}, {self.last_name}"

    def validate_user_info(self) -> bool:
        
        return False