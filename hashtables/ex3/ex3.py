def intersection(arrays):
    """
    YOUR CODE HERE
    """
    # Your code here

    # Create cache and result.
    cache = {}
    result = []

    # Word count approach.
    for i in arrays:
        for j in i:
            if j in cache:
                cache[j] += 1
            else:
                cache[j] = 1

    # If any x has value of more than 1, it is added to result.
    for x in cache:
        if cache[x] > 1:
            result.append(x)

    return result


if __name__ == "__main__":
    arrays = []

    arrays.append(list(range(1000000, 2000000)) + [1, 2, 3])
    arrays.append(list(range(2000000, 3000000)) + [1, 2, 3])
    arrays.append(list(range(3000000, 4000000)) + [1, 2, 3])

    print(intersection(arrays))
