import os
import re


def parse_function(name, tab):
    names = []
    names_splitted = []

    function_list = []
    actual_name = []

    if os.path.isfile(name):
        with open(name) as file:  # there is no need to close the file. "with" statement do this by itself
            for x in file:
                re.sub('\s+', ' ', x).strip()  # Handling extra space's in line
                if x.startswith("def"):
                    names.append(x)

            for x in names:
                words = x.split()  # Dividing line into words(creating a list o words)
                names_splitted.append(words[1].strip())  # adding only file name to main list
                actual_name = names_splitted[0].split("(")

        for x in tab:
            if len(actual_name) and x != actual_name[0]:
                counter = 0
                with open(name) as file:
                    for b in file:
                        if x + "(" in b:
                            counter = counter + 1
                    if counter > 0:
                        tup1 = (actual_name[0], x, counter)

                        function_list.append(tup1)

        return function_list

    else:
        print("This is not a File.")
        return []




