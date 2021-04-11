from src.Node import Node
from src.extract_nodes import extract_nodes


def assert_nodes_parsed_correctly():
    node0 = Node('0')
    node0.in_degree = 0
    node0.out_degree = 2

    node1 = Node('1')
    node1.in_degree = 1
    node1.out_degree = 0

    node2 = Node('2')
    node2.in_degree = 1
    node2.out_degree = 0

    expected_nodes = [node0, node1, node2]

    edges = [{'source': '0', 'target': '2'}, {'source': '0', 'target': '1'}]
    actual_nodes = extract_nodes(edges)
    actual_nodes.sort(key=lambda node: node.id)

    should_be_true = True
    for i in range(len(actual_nodes)):
        actual_node = actual_nodes[i]
        expected_node = expected_nodes[i]
        should_be_true = should_be_true \
                         and (expected_node.id == actual_node.id) \
                         and (expected_node.in_degree == actual_node.in_degree) \
                         and (expected_node.out_degree == actual_node.out_degree)
    return should_be_true


assert assert_nodes_parsed_correctly()
