def register_user(database):
    name = input("Enter your name: ")
    email = input("Enter your email id: ")
    rollnum = input("Enter your roll number: ")
    password = input("Enter your password:")

    if rollnum in database:
        print("Roll number already exists. Please try again.")
    else:
        database[rollnum] = {'name': name, 'email': email, 'password': password}
        print("Registration successful!")

def login_user(database):
    rollnum = input("Enter your roll number: ")
    if rollnum in database:
        password = input("Enter your password: ")
        if database[rollnum]['password'] == password:
            print("Welcome,", database[rollnum]['name'])
            print("Email:", database[rollnum]['email'])
        else:
            print("Incorrect Password. Please try again.")
    else:
        print("Invalid Roll Number. Please try again.")

#Driver Code
database = {}
while True:
    print("\nOptions:")
    print("1. Register")
    print("2. Login")
    print("3. Display user details")
    print("4. Quit")

    choice = input("Enter your choice: ")

    if choice == '1':
        register_user(database)
    elif choice == '2':
        login_user(database)
    elif choice == '3':
        rollnum = input("Enter the roll number to display details: ")
        if rollnum in database:
            print("Name:", database[rollnum]['name'])
            print("Email:", database[rollnum]['email'])
        else:
            print("User not found.")
    elif choice == '4':
        print("Exiting the program.")
        break
    else:
        print("Invalid choice. Please try again.")
