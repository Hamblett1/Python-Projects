number = 10
if number > 15:
    print("the number is bigger than 10")
else:
    print("the number is less than 15")

age = int(input("please enter your age:"))
if age > 17:
    print("you can proceed")
if age > 10:
    print("you can proceed")

else:
    print("You may not proceed")

name = (input("please enter your name"))
if len(name) > 10:
    print("you cannot proceed")
else:
    print("you can proceed")

# The elif keyword is used in conditional statements (if statements), and is short for else if.
# For example
if 10 < 5:
    print("false, this block will not be executed")
elif 0 < 5:
    print("True, block will be executed")
elif 0 < 3:
    print("True, but this will not be executed")
else:
    print("If all fails, execute this")
