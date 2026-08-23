print("=" * 50)
print("Simple Calculator")
print("=" * 50)

number1 = float(input("Enter the first number: "))
operator = input("Enter an operator (+, -, *, /): ")
number2 = float(input("Enter the second number: "))

if operator == "+":
    result = number1 + number2
elif operator == "-":
    result = number1 - number2
elif operator == "*":
    result = number1 * number2
elif operator == "/":
    if number2 != 0:
        result = number1 / number2
    else:
        result = "Error: Division by zero"
else:
    result = "Error: Invalid operator"

print("Result:", result)

