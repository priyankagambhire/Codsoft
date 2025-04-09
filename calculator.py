def calculator():
    print("Simple Calculator")
    print("Choose an operation: ")
    print("1. Addition (+)")
    print("2. Subtraction (-)")
    print("3. Multiplication (*)")
    print("4. Division (/)")
    try:
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
        operation = input("Enter the operation (+, -, *, /): ")
        if operation == '+':
            result = num1 + num2
        elif operation == '-':
            result = num1 - num2
        elif operation == '*':
            result = num1 * num2
        elif operation == '/':
            if num2 == 0:
                print("Error! Division by zero is not allowed.")
                return
            result = num1 / num2
        else:
            print("Invalid operation. Please choose a valid operation.")
            return

        print(f"Result: {num1} {operation} {num2} = {result}")

    except ValueError:
        print("Invalid input! Please enter numeric values.")

calculator()