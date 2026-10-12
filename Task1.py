# python_calc.py

def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


def multiply(a, b):
    return a * b


def divide(a, b):
    if b == 0:
        return "Error! Cannot divide by zero."
    return a / b


def power(a, b):
    return a ** b


def check_even_odd(number):
    if number % 2 == 0:
        return "Even"
    else:
        return "Odd"


def calculate_percentage(number, total):
    if total == 0:
        return "Error! The second number cannot be zero."
    return (number / total) * 100


while True:
    print("\n===== My Python Calculator =====")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Check Even/Odd")
    print("6. Calculate Percentage")
    print("7. Calculate Power")
    print("8. Exit")

    choice = input("Choose an option (1-8): ")

    if choice == "8":
        print("Calculator closed. Goodbye!")
        break

    elif choice == "5":
        try:
            number = int(input("Enter a whole number: "))
            print(f"The number is {check_even_odd(number)}.")
        except ValueError:
            print("Invalid input! Please enter a whole number.")

    elif choice in ["1", "2", "3", "4", "6", "7"]:
        try:
            num1 = float(input("Enter the first number: "))
            num2 = float(input("Enter the second number: "))

            if choice == "1":
                result = add(num1, num2)
            elif choice == "2":
                result = subtract(num1, num2)
            elif choice == "3":
                result = multiply(num1, num2)
            elif choice == "4":
                result = divide(num1, num2)
            elif choice == "6":
                result = calculate_percentage(num1, num2)
            elif choice == "7":
                result = power(num1, num2)

            if choice == "6":
                if isinstance(result, (int, float)):
                    print(f"Percentage: {result:.2f}%")
                else:
                    print(result)
            elif choice in ["1", "2", "3", "4", "7"]:
                print("Result:", result)

        except ValueError:
            print("Invalid input! Please enter valid numbers.")

    else:
        print("Invalid choice! Please select an option from 1 to 8.")