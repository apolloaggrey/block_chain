from classes import *


class Graph():
    """docstring for Graph"""
    Nodes = Node.nodes
    Edges = Edge.edges

    def __init__(self):
        super(Graph, self).__init__()
        pass

    def __str__(self):
        # for node in Graph.Nodes:
        #     print("-----------" + Graph.Nodes[node].name + "-----------")
        #     print(Graph.Nodes[node], ":", Graph.Nodes[node].children)
        #     Graph.Nodes[node].get_children()
        graph = F"{[Graph.Nodes[node].name for node in Graph.Nodes]}\n"
        for edge in Graph.Edges:
            graph += str(Graph.Edges[edge]) + "\n"
        return (graph)
        pass


def main():

    nairobi = Node("nairobi")
    mombasa = Node()
    kisumu = Node("kisumu")
    mombasa.name_node("mombasa")
    mombasa.join(kisumu, 3)
    nk = Edge(nairobi, "kisumu", 4, "<")
    vk = Edge("voi", "kisumu", 5, ">")
    nairobi.join(mombasa, 7, "<")
    kv = Edge(kisumu, "voi")

    towns = Graph()
    print(towns)
    pass


if __name__ == '__main__':
    try:
        main()
        pass
    except Exception as e:
        raise e
