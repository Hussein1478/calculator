def main():
    print("Welcome to the Simple Calculator!")
    print("Available operations: +, -, *, /")
    print("-" * 30)
    
    try:
        # Get the first number
        num1 = float(input("Enter the first number: "))
        
        # Get the second number
        num2 = float(input("Enter the second number: "))
        
        # Get the operation
        operation = input("Enter the operation (+, -, *, /): ").strip()
        
        # Perform the calculation based on the operation
        if operation == '+':
            result = num1 + num2
            print(f"{num1} + {num2} = {result}")
        elif operation == '-':
            result = num1 - num2
            print(f"{num1} - {num2} = {result}")
        elif operation == '*':
            result = num1 * num2
            print(f"{num1} * {num2} = {result}")
        elif operation == '/':
            if num2 == 0:
                print("Error: Division by zero is not allowed!")
            else:
                result = num1 / num2
                print(f"{num1} / {num2} = {result}")
        else:
            print("Error: Invalid operation! Please use +, -, *, or /")
    
    except ValueError:
        print("Error: Please enter valid numbers!")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    main()