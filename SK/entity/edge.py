class Edge:
    def __init__(self, fromNode, toNode, weight):
        self.fromNode = fromNode
        self.toNode = toNode
        self.weight = weight

    def repr(self):
        return "%s -> %s : %d" % (self.fromNode, self.toNode, self.weight)