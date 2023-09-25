from pydantic import BaseModel

class User(BaseModel):
    name: str
    age: int
    email: str | None

# Create an instance of the User class
user_data = {
    "name": "John Doe",
    "age": 30,
    "email": "johndoe@example.com"
}

user = User(**user_data)

# Access the validated data
print(user.name)    # Output: John Doe
print(user.age)     # Output: 30
print(user.email)   # Output: johndoe@example.com

print(user.model_dump()) 
# {
#     "name": "John Doe",
#     "age": 30,
#     "email": "johndoe@example.com"
# }
