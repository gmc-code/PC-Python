from dataclasses import dataclass


# Define the User dataclass
@dataclass
class User:
    name: str
    age: int


# Function to validate and create a user from input
def create_user(name_input: str, age_input: str) -> User:
    name = name_input.strip()
    if not name:
        raise ValueError("Name is required.")

    if not age_input.strip().isdigit():
        raise ValueError("Age must be a number.")

    age = int(age_input)
    if not (0 <= age <= 120):
        raise ValueError("Age must be between 0 and 120.")

    return User(name=name, age=age)


# Function to create a default user (for testing/demo)
def create_default_user() -> User:
    return User(name="Alice", age=25)


# Main program
if __name__ == "__main__":
    try:
        user = create_user(input("Enter name: "), input("Enter age: "))
        print(f"Created user from input: {user}")
    except ValueError as e:
        print("Validation error:", e)

    # Also create and print a default user
    default_user = create_default_user()
    print(f"Default user: {default_user}")
