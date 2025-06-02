# arithmetic_operation
def perform_operation(num1, num2, operation):
    num1 = float(input("Enter the first number"))
    num2 = float(input("Enter thr second number"))
    if operation == 'add':
        return num1 + num2
    elif operation == 'subtract':
        return num1 - num2
    elif operation == 'multiply':
        return num1 * num2
    elif operation == 'divide':
        if num2 == 0:
            return "Error: Division by zero"
        return num1 / num2
    else:
        return "Error: Invalid operation"
    