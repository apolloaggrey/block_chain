import Edge
# import random


class Node(object):
    """docstring for Node"""
    nodes = {}

    # def __init__(self, x, y):
    #     pass

    def __init__(self, name=None):
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
        return(self.name)
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
            node = Node.Node(name)
            return node
            pass

    def join(self, node, size=1, direction="<>"):
        if type(node) == str:
            self.node = self.create_node()
        else:
            self.node = node
        new_edge = Edge.Edge(self, self.node, size, direction)
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


def main():
    nairobi = Node("nairobi")
    mombasa = Node()
    kisumu = Node("kisumu")
    mombasa.name_node("mombasa")
    mombasa.join(kisumu)
    nk = Edge.Edge(nairobi, "kisumu", 400)
    vk = Edge.Edge("voi", "kisumu", 450, ">")
    nairobi.join(mombasa, 540)
    kv = Edge.Edge(kisumu, "voi")
    # kisumu = Node("kisumu")
    for node in Node.nodes:
        print(Node.nodes[node].name + "-----------")
        Node.nodes[node].get_children()
    print(nk)
    print(vk)
    print(kv)
    print([Node.nodes[node].name for node in Node.nodes])

    pass


if __name__ == '__main__':
    try:
        main()
        pass
    except Exception as e:
        raise e
