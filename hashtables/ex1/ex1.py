def get_indices_of_item_weights(weights, length, limit):
    """
    It's in the name:
    A Function to get the indices of item weights

    Methodology:
    I will take each item in the weights and subtract that from the limit
    to get a difference. 
    Then I will check to see if any of the items in weights, when added
    to the difference, equal the limit.  Each time one is successfully
    found I will append it.

    Then, for proper format, I will take the higher of the two values 
    and place them in position 0, as instructions asked me to. 
    """
    idx = []
    lookup = {}
    if length > 1:
        for i in range(length):
            lookup[weights[i]] = limit - weights[i]
            if lookup[weights[i]] in weights:
                idx.append(i)
    
    if len(idx) > 1:
        if idx[0] > idx[1]:
            return (idx[0], idx[1])
        else:
            return (idx[1], idx[0])
