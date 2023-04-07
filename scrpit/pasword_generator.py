letter = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '_', '+']
import random
print("Welcome to PY password generator")
nr_letter = int(input("how many letter would you like in your password?\n"))
nr_symbols = int(input("how many symbols would you like?\n"))
nr_numbers = int(input("How many numbers would you like?\n"))
password_list = []
password = ""


# Easy level

# for char in range(1, nr_letter + 1):
#     password += random.choice(letter)
# for num in range(1, nr_numbers + 1 ):
#     password += random.choice(numbers)
# for sym in range(1, nr_symbols + 1 ):
#     password += random.choice(symbols)
# print(password)


# Hard level

for char in range(1, nr_letter + 1):
    password_list.append(random.choice(letter))
for num in range(1, nr_numbers + 1 ):
    password_list.append(random.choice(numbers))
for sym in range(1, nr_symbols + 1 ):
    password_list.append(random.choice(symbols))
random.shuffle(password_list)
for char in password_list:
    password += char
print(f"your password is: {password}")