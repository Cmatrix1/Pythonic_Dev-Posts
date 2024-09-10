class Database:
    def connect(self):
        return "Connected to the database"

class UserService:
    def __init__(self, database):
        # Database instance is injected via the constructor
        self.database = database
    
    def get_user(self, user_id):
        # Using the injected Database instance
        connection = self.database.connect()
        print(f"{connection} to fetch user with ID {user_id}")
        return f"User {user_id}"

# Usage
database = Database()
user_service = UserService(database)  # Injecting the Database instance
user_service.get_user(1)
