
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

print("\nSelect operation:")
print("1. Addition (+)")
print("2. Subtraction (-)")
print("3. Multiplication (*)")
print("4. Division (/)")

choice = input("\nEnter choice (+, -, *, /): ")


if choice == '+':
    result = num1 + num2
    print("the Addition of the 2 numbers is: ",result)

elif choice == '-':
    result = num1 - num2
    print("the Subtraction of the 2 numbers is: ",result)

elif choice == '*':
    result = num1 * num2
    print("the Multiplication of the 2 numbers is: ",result)

elif choice == '/':
    if num2 != 0:
        result = num1 / num2
        print("the Divide of the 2 numbers is: ",result)
    else:
        print("Error: Division by zero is not allowed!")

else:
    print("Invalid input! Please choose a valid operation.")
