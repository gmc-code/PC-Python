# with typing for clarity
# --Optional[int]: This means the function might return an int or None (if validation fails).

from typing import Optional

def get_valid_age(age_input: str) -> Optional[int]:
    """Validates age input: existence, type, range."""
    age_input = age_input.strip()

    # Existence check
    if not age_input:
        print("Error: Age is required.")
        return None

    # Type check
    if not age_input.isdigit():
        print("Error: Age must be a number.")
        return None

    age = int(age_input)

    # Range check
    if not (0 <= age <= 120):
        print("Error: Age must be between 0 and 120.")
        return None

    return age

# Example usage
user_input: str = input("Enter your age: ")
validated_age: Optional[int] = get_valid_age(user_input)

if validated_age is not None:
    print(f"Validated age: {validated_age}")
