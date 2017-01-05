filename = "learning_python.txt"

with open(filename) as file_object:
    for line in file_object:
        new_line = line.replace("Python", "C")
        print(new_line.rstrip())