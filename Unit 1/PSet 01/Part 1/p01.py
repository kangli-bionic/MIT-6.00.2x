"""Greedy cow transport."""


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


cows = {
    'Polaris': 20,
    'Patches': 60,
    'Louis': 45,
    'Horns': 50,
    'Clover': 5,
    'Lotus': 10,
    'Miss Bella': 15,
    'MooMoo': 85,
    'Muscles': 65,
    'Milkshake': 75
}
limit = 100
r = greedy_cow_transport(cows, limit)
print(r)
