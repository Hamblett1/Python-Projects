cars = ["BMW", "Mercedes", "Ford"]

for car in cars:
    print("Car:", car)

for time in range(2):
    print("How are you?\nI'm fine")

# print a letter 50 times

for letter in range(50):
    print("x", end="$")

sports = ["\nRugby", "Cricket", "Tennis", "Afl"]

for sport in sports:
    print(sport)
print(sports[2])

word = input("Enter a word: ")
for letter in word:
    if letter == "n":
        print("The letter n was found in your word")

# n, i and uppercase detector
word = input("\nEnter a word: ")
for letter in word:
    if letter == "n":
        print("The letter n was found in your word")
    if letter == "i":
        print("The letter i was found in your word")
    if letter == letter.upper():
        print("An upper case letter was detected")

# For each character in the word it will check each of the if statements because of the for function.
