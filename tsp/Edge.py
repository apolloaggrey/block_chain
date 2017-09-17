import Node


class Edge(object):
    """docstring for Edge"""
    edges = {}

    def __init__(self, node1, node2, size=1, direction="<>"):
        super(Edge, self).__init__()

        if type(node1) == str:
            self.node1 = self.create_node(node1)
        else:
            self.node1 = node1

        if type(node2) == str:
            self.node2 = self.create_node(node2)
        else:
            self.node2 = node2

        self.size = int(size)
        if "<" in str(direction) and ">" in str(direction):
            self.direction = f"<-{self.size}->"
        elif "><" in str(direction):
            self.direction = None
        elif "1" in str(direction) and "2" in str(direction):
            self.direction = f"<-{self.size}->"
        elif "1" in str(direction) or "<" in str(direction):
            self.direction = f"<-{self.size}-"
        elif "2" in str(direction) or ">" in str(direction):
            self.direction = f"-{self.size}->"
        else:
            self.direction = f"<-{self.size}->"
        self.name = None

        if not self.is_present():
            Edge.edges.update([(len(Edge.edges), self)])
            self.node1.edges.append(self)
            self.node1.children.append(self.node2)
            self.node2.edges.append(self)
            self.node2.children.append(self.node1)
            self.name = str(self.node1) + self.direction + str(self.node2)
            pass
        else:
            self.name = str(self.node1) + self.direction + str(self.node2)
            return
    pass

    def __str__(self):
        return(self.name)

    def create_node(self, name):
        presence = Node.Node.is_present(self, name)
        if presence is False:
            node = Node.Node(name)
            return node
        else:
            return presence
    pass

    def is_present(self):
        for node in Node.Node.nodes:
            if Node.Node.nodes[node].name == self.node1.name:
                for child in Node.Node.nodes[node].children:
                    if child.name == self.node2.name:
                        return(True)
            if Node.Node.nodes[node].name == self.node2.name:
                for child in Node.Node.nodes[node].children:
                    if child.name == self.node1.name:
                        return(True)
        else:
            return(False)
    pass

