"""Unit 1 - Lecture 2 - DP."""

import random


class Item(object):
    """Item."""

    def __init__(self, n, v, w):
        """Initialize item."""
        self._name = n
        self._value = float(v)
        self._weight = float(w)

    @property
    def name(self):
        return self._name

    @property
    def value(self):
        return self._value

    @property
    def weight(self):
        return self._weight

    def __str__(self):
        """STR rep."""
        # return self.name
        return '<' + self.name + ', ' + str(self.value) + ', '\
            + str(self.weight) + '>'

    def __repr__(self):
        """Representation."""
        return str(self)


def max_val(left_to_consider, available):
    """Return the best solution to the 0/1 Knapsack problem.

    Assume l a list of items and a a weight.
    Return a tuple of the total weight of a solution to the 0/1 knapsack
    problem and the items of that solution.
    """
    if left_to_consider == [] or available == 0:
        result = (0, ())
    elif left_to_consider[0].weight > available:
        result = max_val(
            left_to_consider=left_to_consider[1:],
            available=available
        )
    else:
        next_item = left_to_consider[0]
        with_value, with_items = max_val(
            left_to_consider=left_to_consider[1:],
            available=available - next_item.weight
        )
        with_value += next_item.value
        without_value, without_items = max_val(
            left_to_consider=left_to_consider[1:],
            available=available
        )

        if with_value > without_value:
            result = (with_value, with_items + (next_item,))
        else:
            result = (without_value, without_items)

    return result


def build_large_menu(n, max_val, max_cost):
    items = []
    for i in range(n):
        items.append(Item(
            str(i),
            random.randint(1, max_val),
            random.randint(1, max_cost),
        ))
    return items


menu = build_large_menu(3, 10, 10)
best_option = max_val(menu, 10)
for _ in menu:
    print(_)

print(best_option)
