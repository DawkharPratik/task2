#task 2
def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y != 0:
        return x / y
    else:
        return "Error: Division by zero"

def calculator():
    print("Simple Calculator")
    print("Operations:")
    print("1. Addition (+)")
    print("2. Subtraction (-)")
    print("3. Multiplication (*)")
    print("4. Division (/)")

    try:
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))
        operation_choice = int(input("Enter the operation choice (1-4): "))
    except ValueError:
        print("Invalid input. Please enter valid numbers.")
        return

    if operation_choice == 1:
        result = add(num1, num2)
    elif operation_choice == 2:
        result = subtract(num1, num2)
    elif operation_choice == 3:
        result = multiply(num1, num2)
    elif operation_choice == 4:
        result = divide(num1, num2)
    else:
        print("Invalid operation choice. Please enter a number between 1 and 4.")
        return

    print("Result: ", result)

if __name__ == "__main__":
    calculator()