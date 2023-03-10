# Create and open a file for the purpose of re-writing
file_out = open("file.txt", "w")
file_out.write("This is the first line.\n")
file_out.write("This is the second line.")
file_out.close()

# Create and open a file for the purpose of appending (adding to existing content)
file_out_a = open("file_append.txt", "a")
file_out_a.write("This is the first line\n")
file_out_a.write("This is the second line.\n")
file_out.close()

# Open a file for the purpose of reading
file_in = open("file.txt", "r")
print(file_in.read())
file_in.close()

phonebook_dictionary = {}
phonebook_file_in = open("phonebook.txt", "r")

for line in phonebook_file_in:
    # Store name and phone after extracting them by splitting them using a space
    name, phone = line.split(" ")

    # Use .rstrip() to clean up the new line after each phone number
    # Add and associate a name with a phone number in the dictionary
    phonebook_dictionary[name] = phone.rstrip()

phonebook_file_in.close()

print(phonebook_dictionary)

print("Johns phone number is", phonebook_dictionary["John"])

for name, phone in phonebook_dictionary.items():
    print("Name:", name, "- Phone:", phone)
    print(f"Name: {name:10s} Phone: {phone}")



