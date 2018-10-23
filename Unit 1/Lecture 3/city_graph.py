"""Unit 1 - Lecture 3 - Graph class."""

# Graph abstraction
from graphs import Node, Edge, Graph, Digraph


def build_city_graph(g_type):
    """Return graph of given type."""
    g = g_type()
    cities = (
        'Boston', 'Providence', 'New York', 'Chicago',
        'Denver', 'Phoenix', 'Los Angeles'
    )
    for city in cities:
        g.add_node(Node(city))

    g.add_edge(Edge(g.get_node('Boston'), g.get_node('Providence')))
    g.add_edge(Edge(g.get_node('Boston'), g.get_node('New York')))
    g.add_edge(Edge(g.get_node('Providence'), g.get_node('Boston')))
    g.add_edge(Edge(g.get_node('Providence'), g.get_node('New York')))
    g.add_edge(Edge(g.get_node('New York'), g.get_node('Chicago')))
    g.add_edge(Edge(g.get_node('Chicago'), g.get_node('Denver')))
    g.add_edge(Edge(g.get_node('Denver'), g.get_node('Phoenix')))
    g.add_edge(Edge(g.get_node('Denver'), g.get_node('New York')))
    g.add_edge(Edge(g.get_node('Los Angeles'), g.get_node('Boston')))
    return g

print(build_city_graph(Graph))
print('_' * 20)
print(build_city_graph(Digraph))
