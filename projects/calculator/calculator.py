"""
Project: Simple Calculator
===========================

Create a basic calculator that can:
- Add, subtract, multiply, and divide two numbers
- Handle invalid input
- Display results clearly

This is a beginner-friendly project to practice:
- Functions
- User input
- Control flow
- Error handling
"""

def add(x, y):
    """Add two numbers"""
    return x + y

def subtract(x, y):
    """Subtract two numbers"""
    return x - y

def multiply(x, y):
    """Multiply two numbers"""
    return x * y

def divide(x, y):
    """Divide two numbers"""
    if y == 0:
        return "Error: Cannot divide by zero!"
    return x / y

def calculator():
    """Main calculator function"""
    print("=" * 40)
    print("Simple Calculator")
    print("=" * 40)
    
    while True:
        print("\nOperations:")
        print("1. Add")
        print("2. Subtract")
        print("3. Multiply")
        print("4. Divide")
        print("5. Exit")
        
        choice = input("\nEnter your choice (1-5): ")
        
        if choice == '5':
            print("Thank you for using the calculator!")
            break
        
        if choice not in ['1', '2', '3', '4']:
            print("Invalid choice! Please try again.")
            continue
        
        try:
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))
            
            if choice == '1':
                result = add(num1, num2)
                operation = "+"
            elif choice == '2':
                result = subtract(num1, num2)
                operation = "-"
            elif choice == '3':
                result = multiply(num1, num2)
                operation = "*"
            elif choice == '4':
                result = divide(num1, num2)
                operation = "/"
            
            print(f"\n{num1} {operation} {num2} = {result}")
            
        except ValueError:
            print("Invalid input! Please enter valid numbers.")
        except Exception as e:
            print(f"An error occurred: {e}")

# Run the calculator
if __name__ == "__main__":
    calculator()
