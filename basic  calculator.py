# Basic Calculator Program

# Function to get a valid number from the user
def get_number(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Invalid number. Please enter a valid numeric value.")

# Ask for inputs
num1 = get_number("Enter the first number: ")
operation = input("Enter the operation (+, -, *, /): ")
num2 = get_number("Enter the second number: ")

# Perform the calculation
if operation == "+":
    result = num1 + num2
elif operation == "-":
    result = num1 - num2
elif operation == "*":
    result = num1 * num2
elif operation == "/":
    if num2 != 0:
        result = num1 / num2
    else:
        result = "Error! Division by zero."
else:
    result = "Invalid operation."

# Display result in the assignment's format
print(f"{num1} {operation} {num2} = {result}")