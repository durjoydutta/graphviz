from graphviz import Digraph
from graph_data import adj

topo_order = []
vis = [0] * len(adj)  # Initially all nodes are unvisited
cycle_found = [False]  # Use a list to modify inside functions


def topo(u, adj, vis, topo_order):
    if cycle_found[0]:  # Stop further processing if a cycle is found
        return

    vis[u] = 1  # Marks as visiting

    for v in adj[u]:
        if vis[v] == 0:
            topo(v, adj, vis, topo_order)
        elif vis[v] == 1:
            cycle_found[0] = True  # Mark cycle detected
            return  # Stop DFS

    vis[u] = 2  # Marks as visited
    topo_order.append(u)


def draw(adj):
    global cycle_found  # Ensure we access the global variable

    # Performing topological sort via DFS
    for u in adj:
        if vis[u] == 0:
            topo(u, adj, vis, topo_order)

    if cycle_found[0]:  # Cycle detected, stop sorting
        print("Cycle detected! Topological sorting is not possible.")
        return None

    topo_order.reverse()  # Reverse the order for correct topological sorting

    dot2 = Digraph(format="svg")

    for u, list_v in adj.items():
        for v in list_v:
            dot2.edge(str(u), str(v))

    # Arrange nodes in topological order if no cycle is found
    rank_string = "{rank=same; " + " ".join(str(u) for u in topo_order) + "}"
    dot2.body.append(rank_string)

    for i, u in enumerate(topo_order):
        dot2.node(str(u), label=f"{u}\n({i+1})", style="filled", fillcolor="lightblue")

    return dot2


draw(adj)
