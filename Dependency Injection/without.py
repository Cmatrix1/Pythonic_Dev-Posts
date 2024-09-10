class Database:
    def connect(self):
        return "Connected to the database"

class UserService:
    def __init__(self):
        # Instantiating the Database directly
        self.database = Database()
    
    def get_user(self, user_id):
        # Using the Database instance directly
        connection = self.database.connect()
        print(f"{connection} to fetch user with ID {user_id}")
        return f"User {user_id}"

# Usage
user_service = UserService()
user_service.get_user(1)
