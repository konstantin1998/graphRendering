from src.Node import Node
from src.assign_layer_positions import group_by_levels


def group_by_vertices(nodes):
    groups = {}
    for node in nodes:
        groups[node.id] = node.layer
    return groups


def needs_dummy_vert(edge, node_to_layer_map):
    source = edge['source']
    target = edge['target']
    if abs(node_to_layer_map[source] - node_to_layer_map[target]) > 1:
        return True
    return False


def make_edges(node_ids):
    edges = []
    for i in range(len(node_ids) - 1):
        source = node_ids[i]
        target = node_ids[i + 1]
        edges.append({'source': source, 'target': target})
    return edges


def split_edge(edge, node_to_layer_map, counter):
    source = edge['source']
    target = edge['target']
    nodes = []
    node_ids = [source]

    for i in range(node_to_layer_map[source] + 1, node_to_layer_map[target]):
        counter += 1
        node = Node(str(counter))
        node.layer = i
        nodes.append(node)
        node_ids.append(node.id)
    node_ids.append(target)

    edges = make_edges(node_ids)
    return nodes, edges, counter


def merge_arrays(arr1, arr2):
    for item in arr2:
        arr1.append(item)


def assign_positions_for_dummy_vertices(nodes, dummy_vertices):
    layer_groups = group_by_levels(nodes)

    for vertex in dummy_vertices:
        group = layer_groups[vertex.layer - 1]
        vertex.pos_in_layer = max(group, key=lambda node: node.pos_in_layer).pos_in_layer + 1
        group.append(vertex)


def add_dummy_vertices_and_edges(nodes, edges):
    max_id = int(max(nodes, key=lambda node: int(node.id)).id)
    node_id_to_layer_map = group_by_vertices(nodes)
    edges_to_split = list(filter(lambda edge: needs_dummy_vert(edge, node_id_to_layer_map), edges))
    splited_edges = []
    dummy_vertices = []
    for edge in edges_to_split:
        edges.remove(edge)
        new_nodes, new_edges, max_id = split_edge(edge, node_id_to_layer_map, max_id)
        merge_arrays(splited_edges, new_edges)
        merge_arrays(dummy_vertices, new_nodes)
    assign_positions_for_dummy_vertices(nodes, dummy_vertices)
    merge_arrays(nodes, dummy_vertices)
    merge_arrays(edges, splited_edges)