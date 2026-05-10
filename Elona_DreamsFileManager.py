def read_messages():
    try:
        file = open("dreams.txt", "r")
        print(file.read())
        file.close()
    except:
        print("File not found.")


def add_message():
    message = input("Enter your new message: ")

    file = open("dreams.txt", "a")
    file.write("\n" + message)
    file.close()

    print("Message added!")


def rewrite_file():
    answer = input("Rewrite the file? yes/no: ")

    if answer == "yes":
        new_text = input("Enter new message: ")

        file = open("dreams.txt", "w")
        file.write(new_text)
        file.close()

        print("File successfully rewrited")
    else:
        print("Cancelled.")

print("Welcome to the inspiration program by Earl")

while True:
    print("=========================================")
    print("Enter the indicating number to proceed")
    print("\n1. Read inspiring messages")
    print("2. Add new inspiring messages")
    print("3. Rewrite inspiring messages")
    print("4. Exit the program")

    choice = input("Enter your choice: ")

    if choice == "1":
        read_messages()

    elif choice == "2":
        add_message()

    elif choice == "3":
        rewrite_file()

    elif choice == "4":
        print("Thank You for using my program")
        break

    else:
        print("Invalid choice.")

