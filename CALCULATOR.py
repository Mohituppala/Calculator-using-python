#!/usr/bin/env python
# coding: utf-8

# In[2]:


import math

def perform_arithmetic_operation():
    # Perform arithmetic operations
    print("Arithmetic Operations:")
    try:
        # Get user input for numbers
        number1 = float(input("Enter the first number: "))
        number2 = float(input("Enter the second number: "))
        
        # Display available operations
        print("Select operation:")
        print("1. Addition")
        print("2. Subtraction")
        print("3. Multiplication")
        print("4. Division")
        operation_choice = int(input("Enter your choice (1-4): "))

        if operation_choice == 1:
            result = number1 + number2
            print("Result: {} + {} = {}".format(number1, number2, result))
        elif operation_choice == 2:
            result = number1 - number2
            print("Result: {} - {} = {}".format(number1, number2, result))
        elif operation_choice == 3:
            result = number1 * number2
            print("Result: {} * {} = {}".format(number1, number2, result))
        elif operation_choice == 4:
            if number2 != 0:
                result = number1 / number2
                print("Result: {} / {} = {}".format(number1, number2, result))
            else:
                print("Error: Cannot divide by zero!")
        else:
            print("Invalid choice!")
    except ValueError:
        print("Invalid input! Please enter valid numbers.")

def perform_trigonometric_operation():
    # Perform trigonometric operations
    print("Trigonometric Operations:")
    try:
        # Get user input for angle
        angle = float(input("Enter the angle in degrees: "))

        # Display available trigonometric operations
        print("Select operation:")
        print("1. Sin")
        print("2. Cos")
        print("3. Tangent")
        operation_choice = int(input("Enter your choice (1-3): "))

        if operation_choice == 1:
            result = math.sin(math.radians(angle))
            print("Result: sin({}°) = {}".format(angle, result))
        elif operation_choice == 2:
            result = math.cos(math.radians(angle))
            print("Result: cos({}°) = {}".format(angle, result))
        elif operation_choice == 3:
            result = math.tan(math.radians(angle))
            print("Result: tan({}°) = {}".format(angle, result))
        else:
            print("Invalid choice!")
    except ValueError:
        print("Invalid input! Please enter a valid angle in degrees.")

# Main program loop
while True:
    # Display the calculator menu
    print("Calculator Menu:")
    print("1. Arithmetic Operations")
    print("2. Trigonometric Operations")
    print("3. Exit")
    try:
        # Get user choice for the menu
        menu_choice = int(input("Enter your choice (1-3): "))

        if menu_choice == 1:
            perform_arithmetic_operation()
        elif menu_choice == 2:
            perform_trigonometric_operation()
        elif menu_choice == 3:
            print("Exiting the calculator...")
            break
        else:
            print("Invalid choice! Please enter a number between 1 and 3.")
    except ValueError:
        print("Invalid input! Please enter a valid number.")


# In[ ]:




