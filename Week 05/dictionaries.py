my_dictionary = {"firstname": "John", "lastname": "Smith", "postcode": 2000}
# Left side is the key right side is the value

# Get the keys of a dictionary
keys = my_dictionary.keys()
print(keys)

# Type shows the type of variable used
variable = "something"
print(type(variable))

# Get the values of a dictionary
values = my_dictionary.values()
print(values)

# Get the items (pairs) of a dictionary
items = my_dictionary.items()
print(items)

# Get the value of a specific key in the dictionary
the_one = my_dictionary["postcode"]
print(the_one)

# Add a new item (pair) to the dictionary
my_dictionary["phone"] = "0403977913"

print(my_dictionary)

# Use for a loop with .items() to neatly display keys and values of a dictionary
for my_key, my_value in my_dictionary.items():
    print(my_key, my_value)

print(my_dictionary["postcode"])




