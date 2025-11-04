def add_one(x):

    x += 1
    print(f"Inside add_one function, x = {x}")

if __name__== "__main__":
    user_input = input("Enter a number: ")

    try:
        num = int(user_input)
    except ValueError:
        print("Invalid input. Using default value 0.")
        num = 0

    print(f"Before calling add_one, num = {num}")
    add_one(num)
    print(f"After calling add_one, num = {num}")