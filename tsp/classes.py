
class Node(object):
    """docstring for Node"""
    nodes = {}

    # def __init__(self, x, y):
    #     pass

    def __init__(self, name=None) -> object:
        """

        :rtype: object
        """
        super(Node, self).__init__()
        if not self.is_present(name):
            Node.nodes.update([(len(Node.nodes), self)])
        else:
            # name += "-" + str(len(Node.nodes))
            # Node.nodes.update([(len(Node.nodes), self)])
            print(name, "Node Redeclared")
            return
        self.name = name
        self.name_node()
        self.size = 1
        self.edges = []
        self.children = []
        # print([Node.nodes[node].name for node in Node.nodes])

    def __str__(self):
        return self.name
        pass

    def name_node(self, name=None):
        if name is None:
            if self.name is None:
                self.name = ""
                # sequence = (0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 'a', 'b', 'c', 'd', 'e', 'f')
                # for x in range(10):
                #     self.name += str(random.choice(sequence))
                self.name += "Node-" + str(len(Node.nodes) - 1)
            pass
        else:
            self.name = name

    def create_node(self, name):
        if not self.is_present(name):
            node = Node(name)
            return node
            pass

    def join(self, node, size=1, direction="<>"):
        if type(node) == str:
            self.node = self.create_node()
        else:
            self.node = node
        new_edge = Edge(self, self.node, size, direction)
        # self.edges.append(new_edge)
        # self.children.append(node)
        pass

    def is_present(self, name):
        for node in Node.nodes:
            if Node.nodes[node].name == name:
                return Node.nodes[node]
        return False

    def get_children(self):
        for child in self.children:
            print(child.name)
        pass


class Edge(object):
    """docstring for Edge"""
    edges = {}

    def __init__(self, node1, node2, size=1, direction="<>"):
        """

        :rtype: object
        """
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
            self.direction = f"<-{self.size}-<"
        elif "2" in str(direction) or ">" in str(direction):
            self.direction = f">-{self.size}->"
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

    def __str__(self):
        return(self.name)

    def create_node(self, name):
        presence = Node.is_present(self, name)
        if presence is False:
            node = Node(name)
            return node
        else:
            return presence
            pass

    def is_present(self):
        for node in Node.nodes:
            if Node.nodes[node].name == self.node1.name:
                for child in Node.nodes[node].children:
                    if child.name == self.node2.name:
                        return(True)
            if Node.nodes[node].name == self.node2.name:
                for child in Node.nodes[node].children:
                    if child.name == self.node1.name:
                        return(True)
        else:
            return(False)
        pass


def main():
    print([Node.nodes[node].name for node in Node.nodes])
    pass


if __name__ == '__main__':
    try:
        main()
        pass
    except Exception as e:
        raise e
