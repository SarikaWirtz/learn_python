#1 Hello world

print('Hello World!')

#2 Simple Calculator

def add_numbers():
    print("This is addition")
    
    number1 = int(input("Enter number1:  "))
    number2 = int(input("Enter number2:  "))

    sum = number1 + number2

    print(f"Addition is: { sum }")

def subtraction_numbers():
    print("This is subtraction")
    number1 = int(input("Enter number1:  "))
    number2 = int(input("Enter number2:  "))

    subtraction = number1 - number2

    print(f"Subtraction is: { subtraction }")

def multiplication_numbers():
    print("This is multiplication")
    number1 = int(input("Enter number1:  "))
    number2 = int(input("Enter number2:  "))

    multi = number1 * number2

    return multi


add_numbers()
subtraction_numbers()
multiplication = multiplication_numbers()
print(f"multiplication is:  { multiplication }")

#Odd or Even Checker

def check_odd_or_even():
    number = int(input("Enter number1:  "))
    if number % 2 == 0:
        print(f"your { number } is even")
    else:
        print(f"Your { number } is odd")

check_odd_or_even()
