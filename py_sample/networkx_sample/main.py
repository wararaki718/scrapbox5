import networkx as nx


def main():
    graph = nx.Graph()
    graph.add_node(1, id="1", name="test")
    graph.add_node(5, id="2", name="text")
    graph.add_nodes_from([
        (2, {"id":"3", "name":"a"}),
        (3, {"id":"4", "name":"b"}),
        (4, {"id":"5", "name":"v"})
    ])
    graph.add_edge(1, 5, name="edge", weight=4.9, coef=3.4)
    graph.add_edge(3, 1)
    print(graph.nodes)
    print(graph.edges)
    print(graph.adj)
    print(graph.nodes.data())
    print("DONE")


if __name__ == "__main__":
    main()
