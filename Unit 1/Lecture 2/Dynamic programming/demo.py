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

    Assume left_to_consider a list of items and available a weight.
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


def fast_max_val(left_to_consider, available, memo={}):
    """Return the best solution to the 0/1 Knapsack problem using DP.

    Assume left_to_consider a list of items and available a weight and
    memo the result of previously results of the recursive calls.

    Return a tuple of the total weight of a solution to the 0/1 knapsack
    problem and the items of that solution.
    """
    if(len(left_to_consider), available) in memo:
        result = memo[(len(left_to_consider), available)]
    elif left_to_consider == [] or available == 0:
        result = (0, ())
    elif left_to_consider[0].weight > available:
        result = fast_max_val(
            left_to_consider=left_to_consider[1:],
            available=available,
            memo=memo
        )
    else:
        next_item = left_to_consider[0]
        with_value, with_items = fast_max_val(
            left_to_consider=left_to_consider[1:],
            available=available - next_item.weight,
            memo=memo
        )
        with_value += next_item.value

        without_value, without_items = fast_max_val(
            left_to_consider=left_to_consider[1:],
            available=available,
            memo=memo
        )

        if with_value > without_value:
            result = (with_value, with_items + (next_item,))
        else:
            result = (without_value, without_items)

    memo[(len(left_to_consider), available)] = result
    return result


def build_large_menu(n, max_val, max_cost):
    """Return random menu of n items bounded to the given max value and max cost."""
    items = []
    for i in range(n):
        items.append(Item(
            str(i),
            random.randint(1, max_val),
            random.randint(1, max_cost),
        ))
    return items


def test_knapsack_problem(items, max_cost, algorithm, name):
    """Test the knapsack problem solutions by calling given algorithm."""
    print("\nTesting the {} algorithm with a {}-size problem".format(name, n))
    best_option = algorithm(items, max_cost)
    print(best_option)

import sys
sys.setrecursionlimit(2000)
for n in (5, 10, 1024):
    items = build_large_menu(n, 90, 250)
    test_knapsack_problem(items, 750, fast_max_val, "DP")
    # test_knapsack_problem(items, 750, max_val, "left-first, depth-first tree")
