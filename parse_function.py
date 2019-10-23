import os
import re


def parse_function(name):
    names = []
    names_splitted = []

    if os.path.isfile(name):
        with open(name) as file:  # there is no need to close the file. "with" statement do this by itself
            for x in file:
                if "import " in x:
                    names.append(x)
        for x in names:
            re.sub('\s+', ' ', x).strip()  # Handling extra space's in line
            words = x.split()  # Dividing line into words(creating a list o words)

            names_splitted.append(words[1])  # adding only file name to main list

        return names_splitted
    else:
        print("This is not a File.")
        return []


