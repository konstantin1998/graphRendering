from src.assign_layer_positions import assign_layer_positions, group_by_levels
from src.assign_layers import assign_layers
from src.extract_nodes import extract_nodes


def compare_arrays(arr1, arr2):
    if len(arr1) != len(arr2):
        return False
    for i in range(len(arr1)):
        if arr2[i] != arr1[i]:
            return False
    return True


def assert_right_positions_in_layer():
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
    assign_layer_positions(nodes, edges)
    level_groups = group_by_levels(nodes)

    should_be_true = True
    for group in level_groups:
        actual_positions = list(map(lambda node: node.pos_in_layer, group))
        for position in actual_positions:
            should_be_true = should_be_true and position >= 1
    return should_be_true


assert assert_right_positions_in_layer()
