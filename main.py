print("Welcome to your calculator!")
def display_menu():
    print("Which operation do you want to use?")
    print("1. Addition (+)")
    print("2. Subtraction (-)")
    print("3. Multiplication (*)")
    print("4. Division (/)")
    print("5. Exit")

def calculator():
    while True:
        display_menu()
        choice = input("Enter your choice (1-5): ")

        if choice == '5':
            print("Exiting calculator. Goodbye!")
            break

        if choice in ('1', '2', '3', '4'):
            try:
                num1 = float(input("Enter first number: "))
                num2 = float(input("Enter second number: "))

                if choice == '1':
                    result = num1 + num2
                    print(f"Result: {num1} + {num2} = {result}")
                elif choice == '2':
                    result = num1 - num2
                    print(f"Result: {num1} - {num2} = {result}")
                elif choice == '3':
                    result = num1 * num2
                    print(f"Result: {num1} * {num2} = {result}")
                elif choice == '4':
                    if num2 == 0:
                        print("Error: Division by zero is not allowed.")
                    else:
                        result = num1 / num2
                        print(f"Result: {num1} / {num2} = {result}")
            except ValueError:
                print("Error: Please enter valid numeric inputs.")
        else:
            print("Invalid choice. Please select a valid option from the menu.")

if __name__ == "__main__":
    calculator()