print("=" * 50)
print("Simple Calculator")
print("=" * 50)

while True:
    try:
        number1 = float(input("Enter the first number: "))
        operator = input("Enter an operator (+, -, *, /): ").strip()
        number2 = float(input("Enter the second number: "))

        if operator == "+":
            result = number1 + number2
        elif operator == "-":
            result = number1 - number2
        elif operator == "*":
            result = number1 * number2
        elif operator == "/":
            result = number1 / number2
        else:
            print("Error: Invalid operator")
            continue

        print("Result:", result)
    except ValueError:
        print("Error: Invalid input. Please enter numeric values.")
    except ZeroDivisionError:
        print("Error: Division by zero")

    continue_calculation = input("Do you want to perform another calculation? (yes/no): ").strip().lower()
    if continue_calculation != "yes" and continue_calculation != "y":
        break

