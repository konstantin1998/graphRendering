from src.assign_parents import assign_parents


def group_by_levels(nodes):
    max_level = max(nodes, key=lambda node: node.layer).layer
    groups = [[] for i in range(max_level)]
    for node in nodes:
        groups[node.layer - 1].append(node)
    return groups


def count_position(nodes):
    if len(nodes) == 0:
        return 1
    s = 0
    for node in nodes:
        s += node.pos_in_layer
    return int(s / len(nodes))


def is_occupied(nodes, cur_node):
    for node in nodes:
        if node.pos_in_layer == cur_node.pos_in_layer:
            return True
    return False


def put(nodes, cur_node):
    cur_node.pos_in_layer = count_position(cur_node.parents)
    while is_occupied(nodes, cur_node):
        cur_node.pos_in_layer += 1
    nodes.append(cur_node)


def assign_layer_positions(nodes, edges):
    level_groups = group_by_levels(nodes)
    assign_parents(nodes, edges)

    for i in range(0, len(level_groups)):
        slot = []
        for j in range(len(level_groups[i])):
            node = level_groups[i][j]
            put(slot, node)


