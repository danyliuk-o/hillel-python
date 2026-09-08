import string

user_input = input("Enter two letters separated by a hyphen (e.g. a-f): ")
start_letter, end_letter = user_input.split("-")

start_index = string.ascii_letters.index(start_letter)
end_index = string.ascii_letters.index(end_letter)

result = string.ascii_letters[start_index:end_index + 1]

print(result)
