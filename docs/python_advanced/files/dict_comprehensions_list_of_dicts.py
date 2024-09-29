students = [{"name": "Alice", "math": 85, "science": 92}, {"name": "Bob", "math": 78, "science": 88}, {"name": "Charlie", "math": 90, "science": 85}]

# Dictionary comprehension to calculate average scores
average_scores = {student["name"]: (student["math"] + student["science"]) / 2 for student in students}
print(average_scores)
# output is {'Alice': 88.5, 'Bob': 83.0, 'Charlie': 87.5}


students = [{"name": "Alice", "math": 85, "science": 92, "history": 78}, {"name": "Bob", "math": 78, "english": 88}, {"name": "Charlie", "science": 85, "history": 90, "art": 95}]

# Dictionary comprehension to calculate average scores
average_scores = {student["name"]: sum(score for subject, score in student.items() if subject != "name") / (len(student) - 1) for student in students}

print(average_scores)


students_scores = {
    "Alice": {"math": [85, 90, 88], "science": [92, 85, 87], "history": [78, 80]},
    "Bob": {"math": [78, 82], "english": [88, 90, 85]},
    "Charlie": {"science": [85, 89], "history": [90, 92, 88], "art": [95, 97]},
}

# Dictionary comprehension to calculate average scores for each student
average_scores = {
                student: {subject: round(sum(scores) / len(scores)) for subject, scores in subjects.items()} 
                for student, subjects in students_scores.items()
                  }

print(average_scores)
# {'Alice': {'math': 88, 'science': 88, 'history': 79}, 'Bob': {'math': 80, 'english': 88}, 'Charlie': {'science': 87, 'history': 90, 'art': 96}}

students_scores = {"math": [85, 90, 88], "science": [92, 85, 87], "history": [78, 80]}
average_scores = {subject: round(sum(scores) / len(scores)) for subject, scores in students_scores.items()} 
print(average_scores)
# {'math': 88, 'science': 88, 'history': 79}