"""6.00.2x Problem Set 1: Space Cows."""

from ps1_partition import get_partitions
import time


# ================================
# Part A: Transporting Space Cows
# ================================
def load_cows(filename):
    """Load cows.

    Read the contents of the given file.  Assumes the file contents contain
    data in the form of comma-separated cow name, weight pairs, and return a
    dictionary containing cow names as keys and corresponding weights as values.

    Parameters:
        filename - the name of the data file as a string

    Returns:
        a dictionary of cow name (string), weight (int) pairs

    """
    cow_dict = dict()

    f = open(filename, 'r')

    for line in f:
        line_data = line.split(',')
        cow_dict[line_data[0]] = int(line_data[1])
    return cow_dict


# Problem 1
def greedy_cow_transport(cows, limit):
    """Return the trips of the spaceship."""
    cows = [(k, v) for k, v in cows.items()]
    cows = sorted(cows, key=lambda x: x[1], reverse=True)
    trips = []
    current_trip = []
    current_weight = 0
    index = 0
    while cows:
        cow = cows[index]
        if current_weight + cow[1] <= limit:
            current_trip.append(cow[0])
            current_weight += cow[1]
            cows.remove(cow)
        else:
            index += 1

        if index == len(cows):
            trips.append(current_trip)
            current_trip = []
            current_weight = 0
            index = 0

    return trips


# Problem 2
def brute_force_cow_transport(cows, limit):
    """Brute force cow transport."""
    min_partitions = len(cows)
    best_partition = []
    for partition in get_partitions(cows.keys()):
        if len(partition) <= min_partitions:
            for trip in partition:
                valid_partition = True
                if sum([cows[k] for k in trip]) > limit:
                    valid_partition = False
                    break
            if valid_partition:
                min_partitions = len(partition)
                best_partition = partition

    return best_partition


# Problem 3
def compare_cow_transport_algorithms():
    """Compare algorithms.

    Using the data from ps1_cow_data.txt and the specified weight limit, run your
    greedy_cow_transport and brute_force_cow_transport functions here. Use the
    default weight limits of 10 for both greedy_cow_transport and
    brute_force_cow_transport.

    Print out the number of trips returned by each method, and how long each
    method takes to run in seconds.

    Returns:
        Does not return anything.

    """
    cows = load_cows("ps1_cow_data.txt")
    limit = 10

    print("Testing greedy algorithm...")
    start_time = time.time()
    greedy_result = greedy_cow_transport(cows, limit)
    end_time = time.time()
    print("\tTime elapsed:", end_time - start_time)
    print("\tTrips returned:", len(greedy_result))

    print("Testing brute force algorithm...")
    start_time = time.time()
    brute_force_result = brute_force_cow_transport(cows, limit)
    end_time = time.time()
    print("\tTime elapsed:", end_time - start_time)
    print("\tTrips returned:", len(brute_force_result))


def test_algorithm(algorithm):
    """Test algorithm."""
    cows = load_cows("ps1_cow_data.txt")
    limit = 100
    print(algorithm(cows, limit))


# test_algorithm(greedy_cow_transport)
# test_algorithm(brute_force_cow_transport)


compare_cow_transport_algorithms()
