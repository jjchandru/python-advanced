while True:
    try:
        age = input("Enter age: ")
        age = int(age)
        print(f"Age is {age}.")
        break
    except ValueError:
        print("Age must be a number.")
