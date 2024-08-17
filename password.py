attempts = 3
while attempts > 0:
    saved_password = "Svovera"
    password = input("Enter your pass: ")

    if password== saved_password:
        print("Connected")
        break
    else:
        print("Wrong password try again")
        attempts = attempts - 1
        print(f"You have {attempts} left")
