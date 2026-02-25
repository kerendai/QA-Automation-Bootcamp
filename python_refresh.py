# Functions
# Function that calculate average from a list
def calculate_avg(values):
    if not values:
        raise ValueError("List is empty")

    for x in values:
        if not isinstance(x, (int, float)):
            raise TypeError(f"Invalid value: {x}")

    return sum(values) / len(values)

# Classes
# A Class of login validator - checks the validity of password
class LoginValidator:
    def __init__(self, username, password):
        self.username = username
        self.password = password
    def is_valid(self):
        if len(self.password) < 8:
            raise ValueError("Password must contain 8 characters")
        if not any(char.isdigit() for char in self.password):
            raise ValueError("Password must contain at least one number")
        return True

# Handling an exception
try:
    validator = LoginValidator("user1", "aaaaaaaaaa1")
    if validator.is_valid():
        print("Login valid")
except ValueError as e:
    print(f"Validation error: {e}")


