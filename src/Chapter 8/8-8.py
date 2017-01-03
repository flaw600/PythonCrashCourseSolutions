def make_album(name, title, num=""):
    album_info = {
        "name": name,
        "title": title
    }

    if num is not "":
        album_info["number"] = num

    return album_info

# one = make_album("One Direction", "Best Song Ever")
# two = make_album("Eminem", "Toy Soldier", "12")
list = []
active = True

while active:
    request = input("Do you want to enter album information? Enter Y/N: ")
    if request is "Y":
        response = {}
        name = input("Enter in the name of the artist: ")
        title = input("Enter in the title of the song: ")
        number = input("Optionally, enter the number of tracks in the album, otherwise just press Enter: ")

        response["name"] = name
        response["title"] = title
        if number is not "":
            response["number"] = number
        list.append(response)
        print("You will now be asked if you want to enter more album information")
    else:
        print("Thank you. Goodbye!")
        active = False

print("\nResults: ")
for dictionary in list:
    for key, value in dictionary.items():
        print(key + ": " + value)
    print()
