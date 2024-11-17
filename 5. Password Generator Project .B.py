# import modules needed --Random Module
import random

# Lists that contains all letters, numbers and symbols for the password generator
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

# user interface code
print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

# password variable:
password = []

# For loops to get the characters in password

# getting the amount letters
for letter in range(1, nr_letters+1):
    password.append(random.choice(letters))

# getting the amount symbols
for symbol in range(1, nr_symbols+1):
    password.append(random.choice(symbols))

# getting the amount numbers
for number in range(1, nr_numbers+1):
    password.append(random.choice(numbers))

# shuffle the password characters randomly 
random.shuffle(password)

# printing the password for the user
print(f"\nyour password is: {''.join(password)}")
