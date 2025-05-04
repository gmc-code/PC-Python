# vce validation

age_input = input("Enter your age: ").strip()

if age_input == "":
    print("Error: Age is required.")
elif not age_input.isdigit():
    print("Error: Age must be a number.")
else:
    age = int(age_input)
    if 0 <= age <= 120:
        print(f"Age accepted: {age}")
    else:
        print("Error: Age must be between 0 and 120.")



