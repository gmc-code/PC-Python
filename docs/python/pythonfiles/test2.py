from typing import get_type_hints


try:
    entry = input('Enter a number between 1 and 30: ')
    num = int(entry)
    num1 = 30/num
    if num > 30:
        raise ValueError(entry)
except ZeroDivisionError as err:
    print(err, "You can't divide by Zero!!!")
except ValueError as err:
    print(err, entry, "Bad Value not between 1 and 30!")
except:
    print("Invalid Input!")
else:
    print("30 divided by", num, "is: ", 30/num)
finally:
    print("**Thank you for playing!**")
