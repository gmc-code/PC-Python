from dataclasses import dataclass
from typing import Optional

@dataclass
class User:
    name: str
    age: int
    email: Optional[str] = None
    is_active: bool = True

    def greet(self) -> str:
        """Return a greeting message."""
        status = "active" if self.is_active else "inactive"
        greeting = f"Hello, {self.name}! You are {self.age} years old and currently {status}."
        if self.email:
            greeting += f" We will contact you at {self.email}."
        else:
             greeting += f" We don't have your email address."
        return greeting


# All fields provided
user1 = User(name="Alice", age=30, email="alice@example.com", is_active=False)

# Optional fields omitted
user2 = User(name="Bob", age=22)

print(user1.greet())
# Output: Hello, Alice! You are 30 years old and currently active. We will contact you at alice@example.com.

print(user2.greet())
# Output: Hello, Bob! You are 22 years old and currently active. We don't have your email address.
