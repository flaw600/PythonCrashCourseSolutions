favorite_places = {
    "p1": ["Texas", "DC"],
    "p2": ["DC", "Las Vegas"],
    "p3": ["Alabama", "Florida"],
}

for person, places in favorite_places.items():
    print("\n" + person + "'s favorite places are: ")
    for place in places:
        print("\t" + place)