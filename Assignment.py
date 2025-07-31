while True:
    # Ask the user for the first number
    num1_input = input("Enter the first number: ")
    if num1_input.strip() == "":
        print("You didn't enter anything.")
        continue
    try:
        num1 = float(num1_input)
    except ValueError:
        print("That's not a valid number.")
        continue

    # Ask the user for the second number
    num2_input = input("Enter the second number: ")
    if num2_input.strip() == "":
        print("You didn't enter anything.")
        continue
    try:
        num2 = float(num2_input)
    except ValueError:
        print("That's not a valid number.")
        continue

    # Ask the user for the operation
    operation = input("Enter an operation (+, -, *, /): ")

    # Perform the operation
    if operation == "+":
        result = num1 + num2
        print(f"{num1} + {num2} = {result}")
    elif operation == "-":
        result = num1 - num2
        print(f"{num1} - {num2} = {result}")
    elif operation == "*":
        result = num1 * num2
        print(f"{num1} * {num2} = {result}")
    elif operation == "/":
        if num2 != 0:
            result = num1 / num2
            print(f"{num1} / {num2} = {result}")
        else:
            print("Error: Cannot divide by zero.")
    else:
        print("Invalid operation. Please enter +, -, *, or /")

    # Ask if the user wants to do another calculation
    again = input("Do you want to calculate again? (yes/no): ")
    if again.lower() != "yes":
        print("Goodbye!")
        break
