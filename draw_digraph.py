from graphviz import Digraph
from graph_data import adj


def drawDigraph(adj):
    # create a graphviz digraph
    dot = Digraph(format="png")

    # add nodes and edges to dot1
    for u, list_v in adj.items():
        dot.node(str(u), style="filled", fillcolor="lightblue")
        for v in list_v:
            dot.edge(str(u), str(v))

    return dot


drawDigraph(adj)
