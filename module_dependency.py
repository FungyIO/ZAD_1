import parse_functions_names
import directory_filenames
import function_parser
from graphviz import Digraph
import functions_cc
import os
import sys

from git_repo_latest_commit_hash import get_git_commit_hash

os.environ["PATH"] += os.pathsep + 'C:/Users/Lenovo/AppData/Local/graphviz-2.38/release/bin'


def module_dependency(path='.'):
    functions_list = parse_functions_names.from_directory(path)
    # print(functions_list)
    file_names = directory_filenames.get_current_directory_filenames(path)
    # print(file_names)
    functions_in_file = {}   # dict [ filename : tab_of_functions_in_this_file ]

    for file_name in file_names:
        functions_in_file[file_name] = parse_functions_names.from_file(file_name)

    module_connections = {}
    fun_to_module_connections_set = set()
    for file_name in file_names:
        function_connection = function_parser.parse_function_2(file_name, functions_list)
        for x in function_connection:
            fun_to_module_connections_set.add((x[0], file_name))

            for file_name_2, functions in functions_in_file.items():
                if file_name is file_name_2:
                    continue
                if x[1] in functions:
                    if (file_name_2, file_name) in module_connections:
                        module_connections[(file_name_2, file_name)] += x[2]
                    else:
                        module_connections[(file_name_2, file_name)] = x[2]

                    fun_to_module_connections_set.add((x[1], file_name_2))

    g = Digraph('his_3', filename='his_3.gv',
                node_attr={'color': 'chocolate1', 'style': 'filled', 'shape': 'tab'})

    if len(sys.argv) >= 3:
        max_num_of_nodes = int(sys.argv[2])
    else:
        max_num_of_nodes = 60

    for edge, counter in module_connections.items():
        g.edge(str(edge[0]), str(edge[1]), label=str(counter))

        max_num_of_nodes -= 1
        if max_num_of_nodes < 0:
            break

    # dodawanie hashu commita do grafu
    commit_hash = get_git_commit_hash(path)
    g.attr(label='Lastest commit hash: ' + commit_hash)
    g.attr(fontsize='20')

    g.attr('node', shape='ellipse', color='khaki')
    g.attr('edge', style='dashed', )

    f_cc = dict(functions_cc.get_all_functions_cc(path))

    for fun_to_module_connection in fun_to_module_connections_set:
        if fun_to_module_connection[0] in f_cc:
            g.edge(fun_to_module_connection[0] + '\n cc ' + f_cc[fun_to_module_connection[0]], fun_to_module_connection[1])
        else:
            g.edge(fun_to_module_connection[0], fun_to_module_connection[1])

        max_num_of_nodes -= 1
        if max_num_of_nodes < 0:
            break

    g.view()


if __name__ == '__main__':
    module_dependency(sys.argv[1])
