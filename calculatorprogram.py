def calculator():
    num1 = float(input("Enter the first number: "))
    operator = input("Enter the operator (+, -, *, /, %): ")
    num2 = float(input("Enter the second number: "))


    if operator == '+':
        result = num1 + num2
    elif operator == '-':
        result = num1 - num2
    elif operator == '*':
        result = num1 * num2
    elif operator == '/':

        if num2 == 0:
            print("Error: Cannot divide by zero.")
            return
        result = num1 / num2
    elif operator == '%':

        if num2 == 0:
            print("Error: Cannot calculate modulus with zero.")
            return
        result = num1 % num2
    else:
        print("Error: Invalid operator.")
        return

    print(f"Result: {num1} {operator} {num2} = {result}")

calculator()

