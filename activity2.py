def checkPassword(correctPassword):
    while True:
        password = input("Enter password: ")
        if password.strip() == "":
            print("Invalid input. Password cannot be blank.")
            continue
        if password == correctPassword:
            print("Access granted.")
            print("Output verified.")
            break
        else:
            print("Incorrect password.")
checkPassword("admin123")
