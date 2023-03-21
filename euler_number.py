import argparse
import networkx as nx
import csv


def read_graph(file):
    # Read graph from .dot file and turn it into a networkx graph
    # https://networkx.org/documentation/stable/reference/generated/networkx.drawing.nx_pydot.read_dot.html
    dot_graph = nx.Graph(nx.drawing.nx_pydot.read_dot(file))

    return dot_graph


def calculate_euler_number(nx_graph):
    # euler number = nodes - edges
    nodes = list(nx_graph.nodes)
    print('Number nodes: ' + str(len(nodes)))
    edges = list(nx_graph.edges)
    print('Number edges: ' + str(len(edges)))

    euler_number = len(nodes) - len(edges)

    print('Euler number: ' + str(euler_number))
    return euler_number


def write_csv(data, output='results.csv'):
    with open(output, 'w', newline='') as csvfile:
        csvwriter = csv.writer(csvfile, delimiter=',', quotechar='|', quoting=csv.QUOTE_MINIMAL)
        csvwriter.writerow(['Euler Number', data])


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Returns the euler number of a .dot graph')
    parser.add_argument('input_file', action='store', type=str, help='.dot file to analyze')
    parser.add_argument('-o', '--output_file', action='store', type=str, required=False, help='Name of output file')

    args = parser.parse_args()

    input_file = args.input_file
    output_file = args.output_file


    graph = read_graph(input_file)

    euler = calculate_euler_number(graph)

    if output_file:
        write_csv(euler, output_file)
    else:
        write_csv(euler)
