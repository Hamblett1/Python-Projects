user_choice = input("Enter l to login or q to quit: ")

while user_choice != "q":
    if user_choice == "l":
        print("Logging you in...")
        break
    else:
        user_choice = input("Enter a choice:")

answer = input("yes or no: ")
while answer != "yes":
    answer = input("yes or no: ")

# ^^^^ This forces someone to say yes

MENU = "L) Login, S) Sign up, Q) Quit"


def get_user_choice():
    print(MENU)
    user_choice = input("Choose [L/S/Q]: ")
    if user_choice == "l":
        print("Logging you in...")
    elif user_choice == "s":
        print("Signing you up...")
    return user_choice


while get_user_choice() != "q":
    get_user_choice()
else:
    print("Quitting the program...")
