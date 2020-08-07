#  Hint:  You may not need all of these.  Remove the unused functions.
class Ticket:
    def __init__(self, source, destination):
        self.source = source
        self.destination = destination


def reconstruct_trip(tickets, length):
    """
    YOUR CODE HERE
    """
    # Your code here

    # Create cache and route.
    cache = {}
    route = [None] * length

    # Loop through our tickets.
    for i in tickets:

        # If our ticket source is none,
        if i.source == "NONE":

            # then we assign route [0]
            route[0] = i.destination
        cache[i.source] = i.destination

    # Loop through the range starting at 1 and the end at given length.
    for x in range(1, length):
        route[x] = cache[route[x - 1]]

    return route
