import json
from pydantic import BaseModel, Field, ValidationError, field_validator

# Define the User model with validation
class User(BaseModel):
    name: str
    age: int = Field(ge=0, le=120)

    @field_validator('name')
    def name_must_not_be_blank(cls, v: str) -> str:
        if not v.strip():
            raise ValueError("Name cannot be blank")
        return v.strip()

# Load data from a file (or API, or external input)
def load_user_from_json(filepath: str) -> User:
    with open(filepath, 'r') as f:
        data = json.load(f)
    return User(**data)  # Pydantic will validate here

# Main program
if __name__ == "__main__":
    try:
        user = load_user_from_json("user_data.json")
        print("✅ Loaded user:", user)
    except ValidationError as e:
        print("❌ Validation errors:")
        print(e.json(indent=2))




❌ Validation errors:
[
  {
    "type": "value_error",
    "loc": [
      "name"
    ],
    "msg": "Value error, Name cannot be blank",
    "input": "  ",
    "ctx": {
      "error": "Name cannot be blank"
    },
    "url": "https://errors.pydantic.dev/2.11/v/value_error"
  },
  {
    "type": "less_than_equal",
    "loc": [
      "age"
    ],
    "msg": "Input should be less than or equal to 120",
    "input": 130,
    "ctx": {
      "le": 120
    },
    "url": "https://errors.pydantic.dev/2.11/v/less_than_equal"
  }
]

'''
