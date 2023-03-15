import random
import string
import time

random_number = random.randint(0, 100)
print("Random number:", random_number)

letters = string.ascii_letters  # Alphabet letters upper & lowercase
digits = string.digits  # All numbers 0-9
symbol = string.punctuation  # All special characters/symbols
characters_combo = letters + digits + symbol  # Add all

print("letters:", letters)
print("digits:", digits)
print("symbols:", symbol)
print("Characters combo:", characters_combo)

random_letter = random.choice(letters)
random_digit = random.choice(digits)
random_symbol = random.choice(symbol)
random_characters_combo = random.choice(characters_combo)  # Pick a random character

print("Random letter:", random_letter)
print("Random digit:", random_digit)
print("Random symbol:", random_symbol)
print("Random character:", random_characters_combo)

character_limit = 10
my_magical_word = ""
for character in range(character_limit):
    my_magical_word += random.choice(characters_combo)
print("My magical word:", my_magical_word)


character_limit = 10
password_generator = ""
for character in range(character_limit):
    password_generator += random.choice(letters+digits)
print("Password:", password_generator)

print("Im quick")
print("Processing...")
time.sleep(20)  # Delay 20 seconds
print("I've taken my time")
print("I'm done")

print("Processing.")
for i in range(5):
    time.sleep(1)
    print(".", end="")
print("\nComplete!")
