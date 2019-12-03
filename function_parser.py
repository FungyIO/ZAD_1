import os
import re


def parse_function_2(filename, tab_of_all_functions):
    names_of_function_in_file_splitted = []
    if os.path.isfile(filename):
        names_of_function_in_file = open_clear_find(filename, 'def')

        for name in names_of_function_in_file:
            words = name.split()
            function_name = words[1].split("(")[0]
            names_of_function_in_file_splitted.append(function_name)

        list_of_dependencies = []
        for x in tab_of_all_functions:
            i = 0
            counter = [0] * len(names_of_function_in_file_splitted)
            with open(filename) as file:
                if (x + "(") not in file.read():
                    continue
                file.seek(0)
                is_line_of_function = False

                for line in file:
                    if line is '\n':  # skips blank lines
                        continue
                    if 'def' + ' ' not in line:
                        if is_line_of_function:
                            if not line.startswith(' ') and not line.startswith('\t'):  # function body must start with ' ' or '\t'
                                is_line_of_function = False
                                continue
                            counter[i] += line.count(x + "(")
                    else:
                        if is_line_of_function is True:
                            i += 1
                        else:
                            is_line_of_function = True

            for actual_function, actual_counter in zip(names_of_function_in_file_splitted, counter):
                if actual_counter != 0:
                    list_of_dependencies.append((actual_function, x, actual_counter))

        return list_of_dependencies

    else:
        print("This is not a File.")
        return []


def open_clear_find(name, word):
    names = []

    with open(name) as file:
        for x in file:
            re.sub('\s+', ' ', x).strip()
            if x.startswith(word):
                names.append(x)
    return names
