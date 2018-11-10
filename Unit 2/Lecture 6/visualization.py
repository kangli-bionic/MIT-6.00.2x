"""Random walks visualization."""

import pylab
import random

from random_walks import Field, Location, UsualDrunk, ColdDrunk
from random_walks import simulate_walks


class StyleIterator(object):
    """Style iterator."""

    def __init__(self, styles):
        """Initialize iterator."""
        self._index = 0
        self._styles = styles

    def next_style(self):
        """Return next style."""
        result = self._styles[self._index]
        if self._index == len(self._styles) - 1:
            self._index = 0
        else:
            self._index += 1
        return result


def simulate_drunk(num_trials, drunk_class, walk_lengths):
    """Simulate drunk walks."""
    mean_distances = []
    for num_steps in walk_lengths:
        print('\tStarting simulation of {} steps'.format(num_steps))
        trials = simulate_walks(num_steps, num_trials, drunk_class)
        mean = sum(trials) / len(trials)
        mean_distances.append(mean)
    return mean_distances


def simulate_all(drunk_kinds, walk_lengths, num_trials):
    """Simulate with multiple drunk types and walk lengths."""
    style_selector = StyleIterator(('m-', 'b--', 'g-.'))

    for drunk_class in drunk_kinds:
        style = style_selector.next_style()
        print('Starting simulation of {}'.format(drunk_class.__name__))
        means = simulate_drunk(num_trials, drunk_class, walk_lengths)
        pylab.plot(walk_lengths, means, style, label=drunk_class.__name__)

    pylab.title('Mean distance from origin ({} trials)'.format(num_trials))
    pylab.xlabel('Number of steps')
    pylab.ylabel('Distance from origin')
    pylab.legend(loc='best')


def get_final_locations(num_steps, num_trials, drunk_class):
    """Return final location."""
    locations = []
    drunk = drunk_class('homer')
    for t in range(num_trials):
        field = Field()
        field.add_drunk(drunk, Location(0, 0))
        for s in range(num_steps):
            field.move_drunk(drunk)
        locations.append(field.locate_drunk(drunk))
    return locations


def plot_locations(drunk_kinds, num_steps, num_trials):
    """Plot ending locations of each drunk."""
    style_selector = StyleIterator(('m+', 'r^', 'mo'))

    pylab.figure('steps', figsize=(13, 13))
    for drunk_class in drunk_kinds:
        locations = get_final_locations(num_steps, num_trials, drunk_class)
        x_vals, y_vals = [], []

        for location in locations:
            x_vals.append(location.x)
            y_vals.append(location.y)

        x_vals = pylab.array(x_vals)
        y_vals = pylab.array(y_vals)
        mean_x = round(sum(abs(x_vals) / len(x_vals)), 5)
        mean_y = round(sum(abs(y_vals) / len(y_vals)), 5)

        style = style_selector.next_style()
        pylab.plot(
            x_vals,
            y_vals,
            style,
            label='{} mean absolute location = <{}, {}>'.format(
                drunk_class.__name__,
                mean_x,
                mean_y
            )
        )

    pylab.title('Location at end of walks ({} steps)'.format(num_steps))
    pylab.ylim(-1000, 1000)
    pylab.xlim(-1000, 1000)
    pylab.xlabel('Steps East/West of origin')
    pylab.ylabel('Steps North/South of origin')
    pylab.legend(loc='upper left')

random.seed(0)
num_steps = (0, 10, 100, 1000, 10000)
simulate_all((UsualDrunk, ColdDrunk), num_steps, 100)

plot_locations((UsualDrunk, ColdDrunk), 10000, 1000)
