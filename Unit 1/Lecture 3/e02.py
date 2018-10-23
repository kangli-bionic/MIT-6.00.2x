"""Unit 1 - Lecture 3 - Exercise 2."""

# Graph abstraction
from graphs import Node, Edge, Graph

nodes = []
nodes.append(Node("ABC"))  # nodes[0]
nodes.append(Node("ACB"))  # nodes[1]
nodes.append(Node("BAC"))  # nodes[2]
nodes.append(Node("BCA"))  # nodes[3]
nodes.append(Node("CAB"))  # nodes[4]
nodes.append(Node("CBA"))  # nodes[5]


g = Graph()
for n in nodes:
    g.add_node(n)


for node in nodes:
    node_name = node.name
    for n in nodes:
        n_name = n.name
        if node_name[:2] == n_name[1::-1] or node_name[1:] == n_name[::-1][:2]:
            if n not in g.children_of(node):
                g.add_edge(Edge(node, n))

for i in range(6):
    edges = g.children_of(nodes[i])
    print(edges)
