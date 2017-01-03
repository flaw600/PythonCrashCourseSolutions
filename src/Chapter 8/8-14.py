def make_car(mf, model, **extra):
    info = {}
    info["mf"] = mf
    info["model"] = model
    for key, value in extra.items():
        info[key] = value
    return info

output = make_car('subaru', 'outback', color='blue', tow_package=True)
for key, value in output.items():
    print("\n" + key + ": " + str(value))