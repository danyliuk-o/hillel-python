import keyword
import string

name = input("Enter a variable name: ")

is_valid = True

if not name or name[0].isdigit():
    is_valid = False

if any(char.isupper() or char.isspace() or (char in string.punctuation and char != "_") for char in name):
    is_valid = False

if name in keyword.kwlist:
    is_valid = False

if "__" in name:
    is_valid = False

print(is_valid)
