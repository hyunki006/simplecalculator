def add(x, y):

    return x + y

def subtract(x, y):

    return x - y

def multiply(x, y):

    return x * y

def divide(x, y):

    return "Error! Division by zero" if y == 0 else x / y

while True:
    print("\nSelect operation!")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")

    choice = input("[1/2/3/4] : ")

    if choice == "5":
        print("Goodbye!")
        break

    num1 = float(input("First number: "))
    num2 = float(input("Second number: "))

    if choice == "1":
        print(f"The answer is: \033[1m{str(add(num1, num2)).rstrip('.0')}\033[m\n")
    elif choice == "2":
        print(f"The answer is: \033[1m{str(subtract(num1, num2)).rstrip('.0')}\033[m\n")
    elif choice == "3":
        print(f"The answer is: \033[1m{str(multiply(num1, num2)).rstrip('.0')}\033[m\n")
    elif choice == "4":
        print(f"The answer is: \033[1m{str(divide(num1, num2)).rstrip('.0')}\033[m\n")
    else:
        print("Invalid choice, choose either 1/2/3/4")




