# Get data from the user
product_name = input("Enter a product name: ")
product_price = input("Enter the price: ")
stock = input("Enter how many in stock: ")

# My Headers
headers = "Product Name, Price, Stock\n"

file_out = open("data.csv", "a")

# Ensure that headers do not exist before you write them
file_in = open("data.csv", "r")
if headers not in file_in:  # If first line doesn't match my headers
    file_in.close()
    file_out.write(headers)  # Headers
else:
    file_in.close()

# Write data
file_out.write(f"{product_name},{product_price},{stock}\n")
file_out.close()
