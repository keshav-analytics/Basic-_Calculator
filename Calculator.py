def add(num1, num2):
    return num1 + num2


def sub(num1, num2):
    return num1 - num2


def multiply(num1, num2):
    return num1 * num2


def divide(num1, num2):
    return num1 / num2


def avg(num1, num2):
    return (num1 + num2) / 2


print("Please select an operation:")
print("1. Addition")
print("2. Subtraction")
print("3. Multiplication")
print("4. Division")
print("5. Average")


select = int(input("Select an operation from 1, 2, 3, 4, 5: "))

number1 = int(input("Enter first number: "))
number2 = int(input("Enter second number: "))


if select == 1:
    print(number1, "+", number2, "=", add(number1, number2))

elif select == 2:
    print(number1, "-", number2, "=", sub(number1, number2))

elif select == 3:
    print(number1, "*", number2, "=", multiply(number1, number2))

elif select == 4:
    if number2 == 0:
        print("Cannot divide by zero!")
    else:
        print(number1, "/", number2, "=", divide(number1, number2))

elif select == 5:
    print("Average =", avg(number1, number2))

else:
    print("Invalid operation! Please select again!")