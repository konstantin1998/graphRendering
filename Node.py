class Node:
    def __init__(self, id):
        self.id = id
        self.layer = -1
        self.pos_in_layer = -1
        self.in_degree = -1
        self.out_degree = -1
        self.parents = []