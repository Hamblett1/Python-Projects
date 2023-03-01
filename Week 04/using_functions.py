def my_calculator():
    print(5 * 5)


my_calculator()


def ask_for_name():
    name = input("Enter your name:")


ask_for_name()


def verify_age():
    age = int(input("Enter your age:"))
    if age >= 18:
        print("You may enter the club")
    else:
        print("Sorry we cannot let you in!")


verify_age()


def verify_age_auto(the_age):
    if the_age >= 18:
        print("You may enter the club")
    else:
        print("Sorry we cannot let you in!")


verify_age_auto(15)


def welcome(someone):
    print("Welcome", someone, "we're excited to see you here.")


welcome("Harry")


def is_adult(an_age):
    if an_age >= 18:
        return True
    else:
        return False


if is_adult(10):
    print("Welcome")
else:
    print("Sorry")


def multiply_by_five(number):
    return 5 * number


print(multiply_by_five(5))

# Refracting and extracting the method will turn the long written code into a function that can be used to save time
