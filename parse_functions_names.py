import os

def parse_function(filename):
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
        return
