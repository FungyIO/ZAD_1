import os


def parse_function(name):
    names = []
    names_splitted = []

    if os.path.isfile(name):
        with open(name) as file:
            for x in file:
                if "import " in x:
                    names.append(x)
        for x in names:
            words = x.split(" ")

            names_splitted.append(words[1])

        return names_splitted
    else:
        print("This is not a File.")
        return []