# Obj: Use a dictionary to store information about a person you know. Store, first/last name, age, city and print them
person1 = {
    "first_name": "flaw",
    "last_name": "600",
    "age": 45,
    "city": "The Internet",
}

person2 = {
    "first_name": "flaw",
    "last_name": "600",
    "age": 45,
    "city": "The Internet",
}

person3 = {
    "first_name": "flaw",
    "last_name": "600",
    "age": 45,
    "city": "The Internet",
}

people = [person1, person2, person3]

for person in people:
    print("This person's first name is: " + person['first_name'] +", last name is: " + person["last_name"] + ", age is: "
      + str(person["age"]) + ", city is: " + person["city"])