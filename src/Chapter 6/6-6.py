favorite_lnguages = {
    "jen": "python",
    "sarah": "c",
    "edward": "ruby",
    "phil": "python",
}

poll = {
    "jen",
    "sarah",
    "edward",
    "phil",
    "jessie",
    "laura"
}

for name in sorted(poll):
    if name in favorite_lnguages:
        print(name + ", your favorite language is: " + favorite_lnguages[name])
    else:
        print(name + ", you should take our poll!")