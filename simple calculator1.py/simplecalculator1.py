# Addition function
def addition(num1, num2):
    return num1 + num2

# Subtraction function
def subtraction(num1, num2):
    return num1 - num2

# Multiplication function
def multiplication(num1, num2):
    return num1 * num2  # Corrected from num1 * num1 to num1 * num2

# Division function
def division(num1, num2):
    if num2 != 0:
        return num1 / num2
    else:
        print("Error: Division by zero is not allowed.")
        return None

# Main function to drive the calculator app
def calculator():
    print("Choose the operation that you want:")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")

    # Ask the user to enter their choice
    choice = input("Enter your choice ('1', '2', '3', '4'): ")

    # Check if the choice exists
    if choice in ['1', '2', '3', '4']:
        try:
            # Ask for the two numbers
            num1 = float(input("Enter the first number please: "))
            num2 = float(input("Enter the second number please: "))

            # Perform the chosen operation
            if choice == '1':
                print(f"{num1} + {num2} = {addition(num1, num2)}")
            elif choice == '2':
                print(f"{num1} - {num2} = {subtraction(num1, num2)}")
            elif choice == '3':
                print(f"{num1} * {num2} = {multiplication(num1, num2)}")
            elif choice == '4':
                result = division(num1, num2)
                if result is not None:
                    print(f"{num1} / {num2} = {result}")
        except ValueError:
            print("Error: Invalid input. Please enter a number.")
    else:
        print("Error: This operation does not exist.")

# Call the calculator function
calculator()
