def getInput():
    user_input = input("Enter Year to check if it's a Leap Year: ")

    while user_input.isdigit() is False or int(user_input) < 0:
        user_input = input("Error, Enter Year to check if it's a Leap Year: ")
    user_input = int(user_input)   
    return user_input

def check_if_leapyear(user_input):
    check = user_input % 4
    if check == 0:
        return True
    else:
        return False

user_input = getInput()
is_leapyear = check_if_leapyear(user_input)

if is_leapyear is True:
    print(f"The year {user_input} is a leap year!")
else:
    print(f"The year {user_input} is not a leap year :(")
