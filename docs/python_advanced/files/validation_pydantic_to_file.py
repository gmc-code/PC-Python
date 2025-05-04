import json
from pydantic import BaseModel, Field, ValidationError, field_validator
from typing import List

class User(BaseModel):
    name: str
    age: int = Field(ge=0, le=120)

    @field_validator('name')
    def name_must_not_be_blank(cls, v: str) -> str:
        if not v.strip():
            raise ValueError("Name cannot be blank")
        return v.strip()


def load_users_from_json(filepath: str, log_path: str) -> List[User]:
    with open(filepath, 'r') as f:
        raw_data = json.load(f)

    users = []
    with open(log_path, 'w') as log_file:
        for idx, record in enumerate(raw_data):
            try:
                user = User(**record)
                users.append(user)
            except ValidationError as e:
                log_file.write(f"\nValidation error in record {idx + 1}:\n")
                log_file.write(e.json(indent=2))
                log_file.write("\n")
    return users


def save_users_to_json(users: List[User], filepath: str) -> None:
    # Convert dataclass-like User objects to plain dicts
    with open(filepath, 'w') as f:
        json.dump([user.model_dump() for user in users], f, indent=2)
    print(f"\n📁 Saved {len(users)} valid user(s) to {filepath}")

# Main
if __name__ == "__main__":
    users = load_users_from_json("user_data_2.json", "user_data_2_log.txt")

    print(f"\n✅ Successfully loaded {len(users)} valid user(s):")
    for user in users:
        print(user)

    if users:
        save_users_to_json(users, "user_data_2_clean.json")
    else:
        print("No valid users to save. See 'user_data_2_log.txt' for details.")
