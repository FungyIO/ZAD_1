import os
import re


def parse_function(name, files):
    names = []
    names_splitted = []

    if os.path.isfile(name):
        with open(name) as file:  # there is no need to close the file. "with" statement do this by itself
            for x in file:
                re.sub('\s+', ' ', x).strip()  # Handling extra space's in line
                if x.startswith("import"):
                    names.append(x)

        for x in names:
            words = x.split()  # Dividing line into words(creating a list o words)

            for (path, dirs, files) in os.walk("."):
                for file in files:
                    if words[1] + ".py" == file:
                        names_splitted.append(words[1] + ".py\n" + str(os.path.getsize(file)))  # adding only file name to main list

        return names_splitted
    else:
        print("This is not a File.")
        return []

