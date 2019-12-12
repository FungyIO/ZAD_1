import os
import directory_filenames


def from_file(filename):
    if os.path.isfile(filename):
        nodes = []
        names = []

        with open(filename) as file:
            for line in file:
                if line.startswith("def"):
                    names.append(line)

            for name in names:
                words = name.split()
                function_name = words[1].split("(")[0]
                nodes.append(function_name)

        return nodes
    else:
        print("There is no such File.")
        return []


def from_directory():
    files = directory_filenames.get_current_directory_filenames()
    nodes = []

    for file in files:
        nodes_from_file = from_file(file)
        for node in nodes_from_file:
            nodes.append(node)

    return nodes
