from src.assign_parents import assign_parents
from src.extract_nodes import extract_nodes


def assert_right_number_of_parents():
    edges = [{'source': '0', 'target': '2'},
             {'source': '0', 'target': '1'},
             {'source': '0', 'target': '3'},
             {'source': '1', 'target': '4'},
             {'source': '4', 'target': '6'},
             {'source': '6', 'target': '7'},
             {'source': '3', 'target': '5'},
             {'source': '5', 'target': '7'},
             {'source': '2', 'target': '7'}]

    nodes = extract_nodes(edges)
    assign_parents(nodes, edges)

    should_be_true = True
    for node in nodes:
        should_be_true = should_be_true and (node.in_degree == len(node.parents))
    return should_be_true


def assert_right_parents():
    edges = [{'source': '0', 'target': '2'},
             {'source': '0', 'target': '1'}
             ]

    nodes = extract_nodes(edges)
    assign_parents(nodes, edges)
    nodes.sort(key=lambda node: node.id)

    return len(nodes[0].parents) == 0 \
        and nodes[1].parents[0] == nodes[0] \
        and nodes[2].parents[0] == nodes[0]


assert assert_right_number_of_parents()
assert assert_right_parents()