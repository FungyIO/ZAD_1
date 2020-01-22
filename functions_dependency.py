import parse_functions_names
import directory_filenames
import function_parser
from graphviz import Digraph
import os
import sys
import functions_cc
os.environ["PATH"] += os.pathsep + 'C:/Users/Lenovo/AppData/Local/graphviz-2.38/release/bin'


def functions_dependency(path='.'):
    functions_list = parse_functions_names.from_directory(path)
    file_names = directory_filenames.get_current_directory_filenames(path)
    function_connections = []
    for f_name in file_names:
        function_connections += function_parser.parse_function_2(f_name, functions_list)

    g = Digraph('unix', filename='unix.gv',
                node_attr={'color': 'aquamarine1', 'style': 'filled'})
    g.attr(size='6,6')

    f_cc = functions_cc.get_all_functions_cc()
    f_cc_dict = dict(f_cc)
    # print(f_cc_dict)

    for edge in function_connections:
        if edge[1] in f_cc_dict:
            g.edge(str(edge[1]) + '\n' + 'cc - ' + f_cc_dict[edge[1]],
                   str(edge[0] + '\n' + 'cc - ' + f_cc_dict[edge[0]]), label=str(edge[2]))

        else:
            g.edge(str(edge[1]), str(edge[0]), label=str(edge[2]))

    g.view()


if __name__ == '__main__':
    functions_dependency(sys.argv[1])
