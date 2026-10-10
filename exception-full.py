try:
    age = input("Enter age: ")
    age = int(age)
    print(f"Age is {age}.")
    age / 0
except ValueError:
    print("Enter valid number")
except ZeroDivisionError:
    print("Cannot divide a number by zero")
else:
    print("A different exception other than ValueError and ZeroDivisionError")
finally:
    print("I always run")
