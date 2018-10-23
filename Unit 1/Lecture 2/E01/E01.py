"""Unit 1, Lecture 2 - Exercise 1."""

import random


class Item(object):
    """Item."""

    def __init__(self, n, v, w):
        """Initialize item."""
        self.name = n
        self.value = float(v)
        self.weight = float(w)

    def getName(self):
        """Return name."""
        return self.name

    def getValue(self):
        """Return value."""
        return self.value

    def getWeight(self):
        """Return weight."""
        return self.weight

    def __str__(self):
        """STR rep."""
        return self.name
        # return '<' + self.name + ', ' + str(self.value) + ', '\
        #     + str(self.weight) + '>'

    def __repr__(self):
        """Representation."""
        return str(self)


def buildItems():
    """Build items."""
    return [Item(n, v, w) for n, v, w in (
        ('clock', 175, 10),
        ('painting', 90, 9),
        ('radio', 20, 4),
        ('vase', 50, 2),
        ('book', 10, 1),
        ('computer', 200, 20))
    ]


def buildRandomItems(n):
    """Build random items."""
    return [Item(
        str(i),
        10 * random.randint(1, 10),
        random.randint(1, 10)
    ) for i in range(n)]


def powerSet(items):
    """Power set."""
    N = len(items)
    # enumerate the 2**N possible combinations
    for i in range(2**N):
        combo = []
        for j in range(N):
            # test bit jth of integer i
            if (i >> j) % 2 == 1:
                combo.append(items[j])
        yield combo


def yieldAllCombos(items):
    """Return all possible combinations of items in two bags."""
    for c1 in powerSet(items):  # c1 stands for combination 1
        for c2 in powerSet(items):  # c2 stands for combination 2
            if (len(set.intersection(set(c1), set(c2))) == 0) or (len(c1) + len(c2) == 0):
                yield (c1, c2)


def pair_combinations(items):
    """Pair."""
    c = []
    for i in items:
        for j in items:
            c.append((i, j))
    return c


items = buildRandomItems(1)
combos = yieldAllCombos(items)

# a = pair_combinations([1, 2, 3])
# print(a)

for c in combos:
    print(c)
