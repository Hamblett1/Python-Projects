import time

# List to store registered users
users = []

# Read existing accounts from file and add to users list
with open("accounts.txt", "r") as file:
    for line in file:
        username, password = line.strip().split(",")
        users.append({"username": username, "password": password})

# Function to validate username and password combination
def validate_login(username, password):
    for user in users:
        if user["username"] == username and user["password"] == password:
            return True
    return False

# Function to handle login option
def login():
    username = input("Enter username: ")
    password = input("Enter password: ")
    if validate_login(username, password):
        print("Login successful!")
    else:
        print("Invalid username or password.")

# Function to handle register option
def register():
    username = input("Enter new username: ")
    while any(user["username"] == username for user in users):
        print("Username already exists. Please enter a different username.")
        username = input("Enter new username: ")
    password_choice = input("Would you like to enter your own password or generate one? (enter/generate): ")
    if password_choice == "enter":
        password = input("Enter password: ")
    elif password_choice == "generate":
        length = int(input("Enter length of password (default is 8): ") or 8)
        characters = ""
        if input("Include numbers? (y/n): ").lower() == "y":
            characters += "0123456789"
        if input("Include symbols? (y/n): ").lower() == "y":
            characters += "!@#$%^&*()_-+={}[]|\:;\"',.<>/?"
        if input("Include lowercase letters? (y/n): ").lower() == "y":
            characters += "abcdefghijklmnopqrstuvwxyz"
        if input("Include uppercase letters? (y/n): ").lower() == "y":
            characters += "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        password = "".join(random.choice(characters) for i in range(length))
        print(f"Generated password: {password}")
    users.append({"username": username, "password": password})
    with open("accounts.txt", "a") as file:
        file.write(f"{username},{password}\n")
    print("Account created successfully.")

# Function to handle view accounts option
def view_accounts():
    if input("Enter admin password: ") == "admin":
        with open("accounts.txt", "r") as file:
            for line in file:
                print(line.strip())
    else:
        print("Incorrect admin password.")

# Main loop to display menu options
while True:
    print("Menu:")
    print("1. Login")
    print("2. Register")
    print("3. View accounts")
