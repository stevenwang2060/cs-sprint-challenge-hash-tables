def has_negatives(a):
    """
    YOUR CODE HERE
    """
    # Your code here

    # Create cache and result.
    cache = {}
    result = []

    # Store all integers in the cache.
    for i in a:
        if i not in cache:
            cache[i] = i

    # Look for the counterpart of the integer.
    for j in cache:
        if cache[j] < 0 and -cache[j] in cache:
            print(-cache[j])
            result.append(abs(cache[j])) # Abs sets the value automatically to postive.

    return result


if __name__ == "__main__":
    print(has_negatives([-1, -2, 1, 2, 3, 4, -4]))
