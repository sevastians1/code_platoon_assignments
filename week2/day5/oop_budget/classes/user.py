from . import budget

class User:
    
    def __init__(self, name, username, password):
        self.name = name
        self.username = username
        self.password = password

    # @classmethod
    def create_user(**user_info):
        return User(**user_info)