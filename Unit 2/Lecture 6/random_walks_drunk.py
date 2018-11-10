"""Location, field and drunk."""

import random


class Location(object):
    """Location in map."""

    def __init__(self, x, y):
        """Coordinates x and y are floats."""
        self._x = x
        self._y = y

    @property
    def x(self):
        """Return x."""
        return self._x

    @property
    def y(self):
        """Return y."""
        return self._y

    def move(self, delta_x, delta_y):
        """Move current location."""
        return Location(self._x + delta_x, self._y + delta_y)

    def distance_from(self, b):
        """Compute distance from another location."""
        x_distance = self._x - b.x
        y_distance = self.y - b.y
        return (x_distance**2 + y_distance**2) ** 0.5

    def __str__(self):
        """Return coordinates."""
        return '<{}, {}>'.format(self._x, self._y)


class Field(object):
    """Field where the drunk moves."""

    def __init__(self):
        """Initialize field."""
        self.drunks = {}

    def add_drunk(self, drunk, location):
        """Add new drunk to the field."""
        if drunk in self.drunks:
            raise ValueError('Duplicated dunk')
        self.drunks[drunk] = location

    def localate_drunk(self, drunk):
        """Return drunk in field."""
        if drunk not in self.drunks:
            raise ValueError('Drunk not in field')
        return self.drunks[drunk]

    def move_drunk(self, drunk):
        """Move drunk in the field."""
        if drunk not in self.drunks:
            raise ValueError('Drunk not in field')
        x_dist, y_dist = drunk.take_step()
        current_location = self.drunks[drunk]
        self.drunks[drunk] = current_location.move(x_dist, y_dist)


class Drunk(object):
    """Drunk."""

    def __init__(self, name):
        """Initialize drunk."""
        self._name = name

    def __str__(self):
        """Return drunk name."""
        return 'This drunk is names {}'.format(self._name)


class UsualDrunk(Drunk):
    """Usual drunk."""

    def take_step(self):
        """Take random walk."""
        step_choices = [(0.0, 1.0), (0.0, -1.0), (1.0, 0.0), (-1.0, 0.0)]
        return random.choice(step_choices)


class ColdDrunk(Drunk):
    """Cold drunk (tries to move to the south since he hates cold)."""

    def take_step(self):
        """Take random walk."""
        step_choices = [(0.0, 0.9), (0.0, -1.1), (1.0, 0.0), (-1.0, 0.0)]
        return random.choice(step_choices)


def walk(field, drunk, num_steps):
    """Assume: field is a Field, drunk a Drunk in field, and num_steps an int >= 0.

    Move drunk num_steps times; returns the distance between the final location
    and the location at the start of the walk.
    """
    start = field.localate_drunk(drunk)
    for s in range(num_steps):
        field.move_drunk(drunk)
    return start.distance_from(field.localate_drunk(drunk))


def simulate_walks(num_steps, num_trials, drunk_class):
    """Assume num_steps an int >= 0, num_trials an int > 0, and drunk_class a subclass of Drunk.

    Simulate num_trials walks of num_steps steps each. Returns a list of the final
    distances for each trial.
    """
    homer = drunk_class('homer')
    origin = Location(0, 0)
    distances = []
    for i in range(num_trials):
        f = Field()
        f.add_drunk(homer, origin)
        distances.append(
            round(
                walk(f, homer, num_steps),
                1
            )
        )
    return distances


def drunk_test(walk_lengths, num_trials, drunk_class):
    """Test random walks.

    Assume walk_lengths a sequence of ints >=0, num_trials an int > 0, and
    drunk_class a subclass of Drunk.

    For each number of steps in walk_lengths, run simulate_walks
    and print results.
    """
    for num_steps in walk_lengths:
        distances = simulate_walks(num_steps, num_trials, drunk_class)
        print('[{}] Random walk of {} steps'.format(
            drunk_class.__name__,
            num_steps
        ))
        print('\tMean = {}'.format(
            round(sum(distances) / len(distances), 4)
        ))
        print('\tMax = {} | Min = {}'.format(
            max(distances),
            min(distances)
        ))


def simulate_all(drunk_kinds, walk_lengths, num_trials):
    """Simulate for all drunk classes."""
    for drunk_class in drunk_kinds:
        drunk_test(walk_lengths, num_trials, drunk_class)

# drunk_test((10, 100, 1000, 10000), 100, UsualDrunk)
# drunk_test((0, 1, 2), 100, UsualDrunk)
simulate_all((UsualDrunk, ColdDrunk), (1, 2, 10, 100, 1000, 10000), 100)
