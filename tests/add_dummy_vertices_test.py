from src.Node import Node
from src.add_dummy_vert import needs_dummy_vert, split_edge, assign_positions_for_dummy_vertices, \
    add_dummy_vertices_and_edges
from src.assign_layer_positions import assign_layer_positions, group_by_levels
from src.assign_layers import assign_layers
from src.extract_nodes import extract_nodes


def assert_needs_dummy_vertex():
    edge1 = {'source': '1', 'target': '4'}
    edge2 = {'source': '1', 'target': '2'}
    node_to_layer_map = {'1': 1, '4': 4, '2': 2}
    return needs_dummy_vert(edge1, node_to_layer_map) and not needs_dummy_vert(edge2, node_to_layer_map)


def assert_split_edge_correctly():
    edge = {'source': '1', 'target': '4'}
    node_to_layer_map = {'1': 1, '4': 4}
    counter = 1
    nodes, edges, counter = split_edge(edge, node_to_layer_map, counter)
    nodes.sort(key=lambda node: node.id)
    edges.sort(key=lambda edge: edge['source'])
    return counter == 3 and nodes[0].id == '2' and nodes[1].id == '3'\
        and len(nodes) == 2\
        and len(edges) == 3 \
        and edges[0]['source'] == '1' and edges[0]['target'] == '2'\
        and edges[1]['source'] == '2' and edges[1]['target'] == '3' \
        and edges[2]['source'] == '3' and edges[2]['target'] == '4'


def assert_dummy_vertices_get_correct_positions():
    nodes = [Node('0'), Node('1')]
    nodes[0].layer = 1
    nodes[0].pos_in_layer = 1
    nodes[1].layer = 2
    nodes[1].pos_in_layer = 2

    dummy_vertices = [Node('2'), Node('3'), Node('4')]
    dummy_vertices[0].layer = 1
    dummy_vertices[1].layer = 2
    dummy_vertices[2].layer = 2
    assign_positions_for_dummy_vertices(nodes, dummy_vertices)

    return dummy_vertices[0].pos_in_layer == 2 \
        and dummy_vertices[1].pos_in_layer == 3\
        and dummy_vertices[2].pos_in_layer == 4


def assert_add_dummy_vertices_correctly():
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
    add_dummy_vertices_and_edges(nodes, edges)

    level_groups = group_by_levels(nodes)
    should_be_true = True
    for group in level_groups:
        actual_positions = list(map(lambda node: node.pos_in_layer, group))
        for position in actual_positions:
            should_be_true = should_be_true and position >= 1

    should_be_true = should_be_true and len(nodes) == 11 and len(edges) == 12
    return should_be_true


assert assert_needs_dummy_vertex()
assert assert_split_edge_correctly()
assert assert_dummy_vertices_get_correct_positions()
assert assert_add_dummy_vertices_correctly()
