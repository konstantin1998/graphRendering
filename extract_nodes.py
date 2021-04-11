from src.Node import Node


def count_in_degree(edges, node_id):
    in_degree = 0
    for edge in edges:
        if edge['target'] == node_id:
            in_degree += 1
    return in_degree


def count_out_degree(edges, node_id):
    out_degree = 0
    for edge in edges:
        if edge['source'] == node_id:
            out_degree += 1
    return out_degree


def extract_nodes(edges):
    node_ids = set()
    for edge in edges:
        node_ids.add(edge['source'])
        node_ids.add(edge['target'])

    nodes = []
    for node_id in node_ids:
        node = Node(node_id)
        node.in_degree = count_in_degree(edges, node_id)
        node.out_degree = count_out_degree(edges, node_id)
        nodes.append(node)

    return nodes
