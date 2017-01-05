active = True

while active:
    response = input("Do you want to enter your name? ")
    filename = "guest_book.txt"
    if response == "Y":
        name = input("What is your name? ")
        print("Welcome, " + name + "!")
        with open(filename, "a") as file_object:
            file_object.write(name + "\n")
    else:
        active = False
