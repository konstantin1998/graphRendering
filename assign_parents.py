def group_by_children(edges):
    groups = {}
    for edge in edges:
        try:
            groups[edge['target']].append(edge['source'])
        except KeyError:
            groups[edge['target']] = [edge['source']]
    return groups


def find_node_by_id(id, nodes):
    for node in nodes:
        if node.id == id:
            return node
    return None


def get_parents(node, nodes, parents_groups):
    try:
        parent_ids = parents_groups[node.id]
        parents = []
        for id in parent_ids:
            parents.append(find_node_by_id(id, nodes))
        return parents
    except KeyError:
        return []


def assign_parents(nodes, edges):
    parents_groups = group_by_children(edges)
    for node in nodes:
        parents = get_parents(node, nodes, parents_groups)
        node.parents = parents