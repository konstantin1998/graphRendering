from scipy.optimize import linprog


def assign_layers(nodes, edges):
    nodes.sort(key=lambda node: int(node.id))
    weights = list(map(lambda node: node.in_degree - node.out_degree, nodes))
    source_node_index = weights.index(min(weights))

    bounds = [(1, len(weights)) for i in range(len(weights))]
    bounds[source_node_index] = (1, 1)

    bound_matrix = []
    for edge in edges:
        source = int(edge['source'])
        target = int(edge['target'])
        koefficients = [0 for j in range(len(weights))]
        koefficients[source] = 1
        koefficients[target] = -1
        bound_matrix.append(koefficients)

    bound_column = [-1.001 for i in range(len(bound_matrix))]
    res = linprog(weights, A_ub=bound_matrix, b_ub=bound_column, bounds=bounds)

    layers = res.x
    for i in range(len(layers)):
        nodes[i].layer = int(layers[i])
