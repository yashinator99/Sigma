class Request:
    def __init__(self, user_id, request_title, request):
        self.user_id = user_id
        self.request_title = request_title
        self.request = request

    def __repr__(self) -> str:
        return f"User Request : id - {self.user_id} request title - {self.request_title} request - {self.request}"

    def validate_request(self) -> bool:
        if len(self.request_title)  < 5 or len(self.request) < 5:
            return False
        elif len(self.request_title) > 40 or len(self.request) > 140:
            return False
        else:
            return True
