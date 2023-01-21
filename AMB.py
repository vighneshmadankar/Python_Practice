messages = []

while True:
    print("Welcome to the Anonymous Message Board!")
    print("1. Leave a message")
    print("2. View messages")
    print("3. Exit")
    choice = input("Enter your choice: ")
    
    if choice == '1':
        message = input("Enter your message: ")
        messages.append(message)
    elif choice == '2':
        for message in messages:
            print(message)
    elif choice == '3':
        break
    else:
        print("Invalid choice. Please try again.")
