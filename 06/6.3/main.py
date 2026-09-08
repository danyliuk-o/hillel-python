import math

input_number = int(input("Enter a number: "))

result = input_number
while result > 9:
    result = math.prod(int(digit) for digit in str(result))

print(result)