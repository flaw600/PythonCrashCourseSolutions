cities = {
    "dallas": {
        "country": "USA",
        "population": "idk",
        "fact": "I don't live here",
    },
    "denver": {
        "country": "USA",
        "population": "How should I know",
        "fact": "I don't live here",
    },
    "tampa": {
        "country": "USA",
        "Population": "IDGAF",
        "fact": "I don't live here"
    }
}

for city, info in cities.items():
    print("City: " + city)
    for key in info:
        print("\t" + key + ": " + info[key])