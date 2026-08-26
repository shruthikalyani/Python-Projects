import math 
history = []
def show_menu():
    print('='*35)
    print('     PYTHON CALCULATOR')
    print('='*35)
    print("Select operation:")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Power")
    print("6. Modulus")
    print("7. Square Root")
    print("8. View History")
    print("9. Exit")
    print('='*35)
while True:
    show_menu()
    choice = input("Enter choice (1-9): ")
    if choice in ['1', '2', '3', '4', '5', '6']:
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
        if choice == '1':
            result = num1 + num2
            operation = f"{num1} + {num2} = {result}"
        elif choice == '2':
            result = num1 - num2
            operation = f"{num1} - {num2} = {result}"
        elif choice == '3':
            result = num1 * num2
            operation = f"{num1} * {num2} = {result}"
        elif choice == '4':
            if num2 != 0:
                result = num1 / num2
                operation = f"{num1} / {num2} = {result}"
            else:
                print("Error: Division by zero!")
                continue
        elif choice == '5':
            result = math.pow(num1, num2)
            operation = f"{num1} ^ {num2} = {result}"
        elif choice == '6':
            result = num1 % num2
            operation = f"{num1} % {num2} = {result}"
        print(operation)
        history.append(operation)
    elif choice == '7':
        num = float(input("Enter a number: "))
        if num >= 0:
            result = math.sqrt(num)
            operation = f"√{num} = {result}"
            print(operation)
            history.append(operation)
        else:
            print("Error: Cannot compute square root of a negative number!")
    elif choice == '8':
        print("Calculation History:")
        for record in history:
            print(record)
    elif choice == '9':
        print("Exiting the calculator. Goodbye!")
        break
    else:
        print("Invalid input. Please enter a number between 1 and 9.")
    