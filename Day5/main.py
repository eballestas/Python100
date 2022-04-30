i#Password Generator Project
import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

value1=""
value2=""
value3=""
passwordresponsehash = ""

for x in letters:
    if nr_letters >= len(value1)+1:
        value1 += x

for x in symbols:
    if nr_symbols >= len(value2)+1:
        value2 += x

for x in numbers:
    if nr_numbers >= len(value3)+1:
        value3 += x

charpool = value1 + value2 + value3

for x in charpool:
    passwordresponsehash += charpool[random.randint(0, len(charpool)-1)]

print(passwordresponsehash)
