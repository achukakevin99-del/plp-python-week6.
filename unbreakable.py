def get_number():
    while True:
        try:
            number = int(input("Enter a whole number: "))
            return number
        except ValueError:
            print("Invalid input. Please enter a whole number.")


def divide_numbers():
    while True:
        try:
            first = int(input("Enter the first number: "))
            second = int(input("Enter the second number: "))
            print("Result:", first / second)
            break
        except ValueError:
            print("Invalid input. Please enter whole numbers.")
        except ZeroDivisionError:
            print("Cannot divide by zero. Try again.")


print("Unbreakable Program")
print("-------------------")

number = get_number()
print("You entered:", number)

divide_numbers()