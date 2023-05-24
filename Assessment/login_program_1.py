import time
import string
import random

accounts_dictionary = {}
file_in = open("accounts.txt","r" )

MENU = "L) Login, R) Register, Q) Quit, V) View accounts"
print(MENU)
user_choice = input("Choose [L/R/Q/V]: ")
def valid_username =
def valid_password =

if user_choice == "L":
    print("Logging you in....")
    entered_username = input("Please enter your username:")
    entered_password = input("Please enter your password:")
    if entered_username == valid_username and entered_password == valid_password:
        print("You have successfully logged in.")
    else:
        print("Invalid credentials.")
elif user_choice == "Q":
    print("Quitting the program...")
elif user_choice == "V":
    print("Loading saved accounts")
elif user_choice == "R":
    print("Starting registration process)")
else:
    print("Invalid choice!")