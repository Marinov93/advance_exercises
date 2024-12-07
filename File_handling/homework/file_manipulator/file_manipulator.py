import os

while True:
    command, *elements = input().split("-")

    if command == 'End':
        break
    elif command == 'Create':
        with open(f"./{elements[0]}", "w"): pass

    elif command == 'Add':
        with open(f"./{elements[0]}", "a") as file:
            file.write(f"{elements[1]}\n")
    elif command == 'Replace':
        try:
            with open(f"./{elements[0]}", "r+") as file_data:
                text = file_data.read()
                text = text.replace(elements[1], elements[2])

                file_data.seek(0)
                file_data.write(text)
                file_data.truncate()
        except FileNotFoundError:
            print("An error occurred")
    elif command == 'Delete':
        try:
            os.remove(f"./{elements[0]}")
        except FileNotFoundError:
            print("An error occurred")