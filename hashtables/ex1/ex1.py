def get_indices_of_item_weights(weights, length, limit):
    """
    YOUR CODE HERE
    """
    # Your code here

    # Create a cache.
    cache = {}

    # Loop through the len of weights list to grab each index value.
    for i in range(len(weights)):

        # Create a current variable to track weight index value.
        current = weights[i]

        # If the weight index value is already in the cache,
        if current in cache:

            # then store that index in a variable that is returned as a tuple.
            needed_weight = cache[current]

            # Returns tuple using the found indices.
            return (i, needed_weight)

        # Stores info about this current weight.
        cache[limit - current] = i

    return None
