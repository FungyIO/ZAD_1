import os
import directory_filenames


def get_function_cc(name_of_function):
    stream = os.popen('radon cc ' + name_of_function)
    output = stream.read()
    fun_and_cc = []
    for l in output.splitlines():
        if ':' in l:
            fun_and_cc.append(tuple((l.lstrip().split(' ')[2], l.lstrip().split(' ')[4])))

    return fun_and_cc


def get_all_functions_cc():
    filenames = directory_filenames.get_current_directory_filenames()
    function_cc = []
    for file in filenames:
        function_cc += get_function_cc(file)

    return function_cc
