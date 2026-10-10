try:
    file = open("sample.txt", "r")
    content = file.read()
    print(content)
except FileNotFoundError:
    print("Error: sample.txt was not found.")
finally:
    file.close()
