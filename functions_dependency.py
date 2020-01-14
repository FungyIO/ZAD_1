import parse_functions_names
import directory_filenames
import function_parser
from graphviz import Digraph
import os
os.environ["PATH"] += os.pathsep + 'C:/Users/Lenovo/AppData/Local/graphviz-2.38/release/bin'

def functions_dependency():
    functions_list = parse_functions_names.from_directory()
    file_names = directory_filenames.get_current_directory_filenames()
    function_connections = []
    for f_name in file_names:
        function_connections += function_parser.parse_function_2(f_name, functions_list)

    g = Digraph('unix', filename='unix.gv',
                node_attr={'color': 'aquamarine1', 'style': 'filled'})
    g.attr(size='6,6')

    for edge in function_connections:
        print(len(edge))
        print(edge)
        g.edge(str(edge[1]), str(edge[0]), label=str(edge[2]))

    g.view()


if __name__ == '__main__':
    functions_dependency()
