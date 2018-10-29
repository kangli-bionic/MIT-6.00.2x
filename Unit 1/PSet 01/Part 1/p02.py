"""Brute force cow transport."""


def get_partitions(l):
    """Pass."""
    return [
        [['Daisy', 'Betsy', 'Buttercup']],
        [['Betsy', 'Buttercup'], ['Daisy']],
        [['Daisy', 'Buttercup'], ['Betsy']],
        [['Buttercup'], ['Daisy', 'Betsy']],
        [['Buttercup'], ['Betsy'], ['Daisy']],
    ]


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


cows = {'Buttercup': 72, 'Betsy': 65, 'Daisy': 50}
limit = 75
r = brute_force_cow_transport(cows, limit)
print(r)
