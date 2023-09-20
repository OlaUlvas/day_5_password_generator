import random

all_letters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L',
               'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X',
               'Y', 'Z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j',
               'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
               'w', 'x', 'y', 'z']
all_symbols = ['!', '"', '#', '€', '%', '&', '/', '(', ')', '=', "^", '*']
all_numbers = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']

letters = int(input("How many letters?: \n"))
symbols = int(input("How many symbols?: \n"))
numbers = int(input("How many numbers?: \n"))

password_list = []
password = ""

for i in range(0, letters):
    password_list.append(random.choice(all_letters))
for i in range(0, symbols):
    password_list.append(random.choice(all_symbols))
for i in range(0, numbers):
    password_list.append(random.choice(all_numbers))



random.shuffle(password_list)

for char in password_list:
    password += char

print(f"\nYour password is {password}")
