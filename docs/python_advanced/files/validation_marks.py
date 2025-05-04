import json
from pydantic import BaseModel, ValidationError, model_validator, confloat, conint
from typing import Literal
import logging

# Predefined subjects
SubjectType = Literal["Science", "Maths", "English"]

# Load student data from the 'student_marks.json' file
try:
    with open('student_marks.json', 'r') as f:
        raw_students = json.load(f)
except FileNotFoundError:
    print("Error: The file 'student_marks.json' was not found.")
    raw_students = []
except json.JSONDecodeError:
    print("Error: The file 'student_marks.json' is not valid JSON.")
    raw_students = []

# Student model with restricted mark range and average check
class Student(BaseModel):
    id: int
    name: str
    surname: str
    student_number: conint(ge=10000, le=99999)  # must be a 5-digit number
    science_marks: confloat(ge=0, le=100)
    maths_marks: confloat(ge=0, le=100)
    english_marks: confloat(ge=0, le=100)
    subject: SubjectType

    @model_validator(mode='before')
    def ensure_average_above_60(cls, values):
        marks = [
            values.get("science_marks"),
            values.get("maths_marks"),
            values.get("english_marks"),
        ]
        if any(m is None for m in marks):
            return values
        avg = sum(marks) / 3
        if avg <= 60:
            raise ValueError(f"Average marks must be over 60%. Got {avg:.2f}%.")
        return values

# Function to determine the subject based on the highest marks
def determine_best_subject(science_marks: float, maths_marks: float, english_marks: float) -> SubjectType:
    marks = {
        "Science": science_marks,
        "Maths": maths_marks,
        "English": english_marks
    }
    best_subject = max(marks, key=marks.get)  # Find the subject with the highest marks
    return best_subject

# Set up logging for invalid students
logging.basicConfig(filename='student_marks_log.txt', level=logging.ERROR)

# Processing the students
valid_students = []
invalid_students = []

for i, raw in enumerate(raw_students):
    raw["id"] = i + 1  # Assign a unique ID to each student
    # Determine the best subject based on highest marks
    raw["subject"] = determine_best_subject(
        raw["science_marks"], raw["maths_marks"], raw["english_marks"]
    )

    try:
        student = Student(**raw)  # Create Student model using raw data
        valid_students.append(student)
        print(f"✅ Valid: {student}")
    except ValidationError as e:
        invalid_students.append(raw)
        logging.error(f"Validation error for student {raw['name']} {raw.get('surname', '')}: {e}")

# Save valid students to JSON
if valid_students:
    with open("students.json", "w") as f:
        json.dump([s.model_dump() for s in valid_students], f, indent=2)
    print(f"\n📁 Saved {len(valid_students)} valid student(s) to 'students.json'")
else:
    print("\n⚠️ No valid students to save.")

# Save invalid students log
if invalid_students:
    print(f"\n⚠️ Invalid students encountered. Check 'student_marks_log.txt' for details.")
else:
    print("\n✅ No invalid students.")
