"""Graph abstraction."""


class Node(object):
    """Node."""

    def __init__(self, name):
        """Assume name is a string."""
        self._name = name

    @property
    def name(self):
        """Return _name value."""
        return self._name

    def __str__(self):
        """Return name."""
        return self._name


class Edge(object):
    """Edge."""

    def __init__(self, src, dest):
        """Assume src and dest are nodes."""
        self._src = src
        self._dest = dest

    @property
    def source(self):
        """Return _source value."""
        return self._src

    @property
    def destination(self):
        """Return _dest value."""
        return self._dest

    def __str__(self):
        """Return direction."""
        return self._src.name + '->' + self._dest.name

    def __repr__(self):
        """Rep call str."""
        return str(self)


class Digraph(object):
    """Represent directed graph."""

    def __init__(self):
        """Initialize without any edges."""
        self.edges = {}

    def add_node(self, node):
        """Add node to edges."""
        if node in self.edges:
            raise ValueError('Duplicated node')
        else:
            self.edges[node] = []

    def add_edge(self, edge):
        """Add edge."""
        src = edge.source
        dest = edge.destination
        if not (src in self.edges and dest in self.edges):
            raise ValueError('Node not in graph')
        self.edges[src].append(dest)

    def children_of(self, node):
        """Return children of given nodes."""
        return self.edges[node]

    def has_node(self, node):
        """Return boolean."""
        return node in self.edges

    def get_node(self, name):
        """Return node if exist."""
        for n in self.edges:
            if n.name == name:
                return n
        raise NameError(name)

    def __str__(self):
        """Return directions."""
        r = ''
        for src in self.edges:
            for dest in self.edges[src]:
                r += src.name + '->' + dest.name + '\n'
        return r[:-1]


class Graph(Digraph):
    """Representation of a graph."""

    def add_edge(self, edge):
        """Override Digraph's implementation."""
        Digraph.add_edge(self, edge)
        rev = Edge(edge.destination, edge.source)
        Digraph.add_edge(self, rev)
