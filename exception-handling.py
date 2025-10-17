# Division by 0

def divide_100_by_user_input():
    user_input = input("Please enter the number:  ")

    try:
        result = float(100/int(user_input))
        print(f"your result is {result}")
    except ZeroDivisionError:
        print("Division by 0 is not possible")
    except ValueError:
        print("Please enter the number")

divide_100_by_user_input()