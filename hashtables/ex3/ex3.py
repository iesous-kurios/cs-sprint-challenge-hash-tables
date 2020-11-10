def intersection(arrays):
    """
    Hi, my name is intersection.  I am 
    a function to find the numbers that exist in 
    every list of arrays you feed me

    """

    cache = {}
    # unpack the list
    for arr in arrays:
        # unpack each array
        for num in arr:
            # append to cache
            if num not in cache:
                cache[num] = 1
            else:
                cache[num] += 1

    result = [k for k, v in cache.items() if v == len(arrays)]
    return result


if __name__ == "__main__":
    arrays = []

    arrays.append(list(range(1000000, 2000000)) + [1, 2, 3])
    arrays.append(list(range(2000000, 3000000)) + [1, 2, 3])
    arrays.append(list(range(3000000, 4000000)) + [1, 2, 3])

    print(intersection(arrays))
