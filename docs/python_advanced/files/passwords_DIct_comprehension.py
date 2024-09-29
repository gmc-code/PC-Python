import string
import random

# Initial lists
ids = [1, 2, 3]
names = ["Alice", "Bob", "Charlie"]

# Function to generate a specific password
def generate_password():
    uppercase_letters = ''.join(random.choice(string.ascii_uppercase) for i in range(2))
    lowercase_letters = ''.join(random.choice(string.ascii_lowercase) for i in range(3))
    digits = ''.join(random.choice(string.digits) for i in range(2))
    punctuation = random.choice(string.punctuation)
    password = uppercase_letters + lowercase_letters + digits + punctuation
    # Randomize the characters in the password
    password = ''.join(random.sample(password, len(password)))
    return password

# Creating the nested dictionary with specific passwords
users = {}
for i in range(len(ids)):
    users[ids[i]] = {"Name": names[i], "Password": generate_password()}

# Printing the nested dictionary
print(users)
