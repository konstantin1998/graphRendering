from src.assign_layers import assign_layers
from src.extract_nodes import extract_nodes


def assert_correct_layers():
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

    assign_layers(nodes, edges)

    expected_layers = [1, 2, 3, 2, 3, 3, 4, 5]

    should_be_true = True
    for i in range(len(expected_layers)):
        should_be_true = should_be_true and (nodes[i].layer == expected_layers[i])

    return should_be_true


assert assert_correct_layers()
