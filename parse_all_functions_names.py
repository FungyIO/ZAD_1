import parse_functions_names
import directory_filenames


def parse_function():
    files = directory_filenames.get_current_directory_filenames()
    nodes = []

    for file in files:
        nodes.append(parse_functions_names.parse_function(file))

    return nodes