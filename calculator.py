def addition(x, y):
    """Returns the sum of two numbers."""
    return x + y

def subtraction(x, y):
    """Returns the difference between two numbers."""
    return x - y

def multiplication(x, y):
    """Returns the product of two numbers."""
    return x * y

def division(x, y):
    """Returns the division of two numbers, handling division by zero."""
    if y == 0:
        # *Fix: Handle the mathematical error
        return "Error: Division by zero is not allowed!"
    return x / y

# ----------------------------------------------------------------------
# MAIN PROGRAM
# ----------------------------------------------------------------------

print("WELCOME TO THE SIMPLE CALCULATOR")
print("Choose an operation:")
print("1. Addition")
print("2. Subtraction")
print("3. Multiplication")
print("4. Division")

while True:
    # Ask for the operation input
    choice = input("Enter your choice (1/2/3/4): ")

    # Check if the choice is valid
    if choice in ('1', '2', '3', '4'):
        try:
            # Ask for the two numbers
            num1 = float(input("Enter the first number: "))
            num2 = float(input("Enter the second number: "))
        except ValueError:
            # *Fix: Handle the error if the input is not a number
            print("Invalid input. Please enter a number.")
            continue  # Return to the beginning of the loop

        if choice == '1':
            result = addition(num1, num2)
        elif choice == '2':
            result = subtraction(num1, num2)
        elif choice == '3':
            result = multiplication(num1, num2)
        elif choice == '4':
            result = division(num1, num2)
        
        # Print the result
        print(f"\nThe result is: {result}\n")
        
        # After calculation, ask if the user wants to continue or exit
        next_calculation = input("Do you want to perform another calculation? (yes/no): ")
        if next_calculation.lower() not in ('yes', 'y'):
            break
    else:
        # *Fix: If the user enters an invalid choice
        print("Invalid choice. Please enter a number from 1 to 4.")

print("Calculator closed. Goodbye!")
