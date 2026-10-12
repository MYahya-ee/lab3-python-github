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


def check_even_odd(number):
    if number % 2 == 0:
        return "Even"
    else:
        return "Odd"


def calculate_percentage(number, total):
    if total == 0:
        return "Error! Cannot calculate percentage when the second number is zero."
    return (number / total) * 100


while True:
    print("\n===== Python Calculator =====")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Check Even/Odd")
    print("6. Calculate Percentage")
    print("7. Exit")

    choice = input("Enter your choice (1-7): ")

    if choice == "7":
        print("Thank you for using the calculator!")
        break

    elif choice == "5":
        try:
            number = int(input("Enter a whole number: "))
            print(number, "is", check_even_odd(number))
        except ValueError:
            print("Error! Please enter a valid whole number.")

    elif choice in ["1", "2", "3", "4", "6"]:
        try:
            num1 = float(input("Enter the first number: "))
            num2 = float(input("Enter the second number: "))

            if choice == "1":
                print("Result:", add(num1, num2))

            elif choice == "2":
                print("Result:", subtract(num1, num2))

            elif choice == "3":
                print("Result:", multiply(num1, num2))

            elif choice == "4":
                print("Result:", divide(num1, num2))

            elif choice == "6":
                print("Percentage:", calculate_percentage(num1, num2), "%")

        except ValueError:
            print("Error! Please enter valid numbers.")

    else:
        print("Invalid choice! Please select a number from 1 to 7.")