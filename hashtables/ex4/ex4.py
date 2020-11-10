def has_negatives(a):
    """
    Hola, me 'llamo has_negatives'.  Mis amigos
    me llaman 'tiene_negativos".  

    """

    # A negative only exists if there is a corresponding
    # positive number

    # if the negative version exists, it will be less
    # than zero

    # return each negative multiplied by -1 
    lookup = {i: -i for i in a if i < 0}
    result = []
    for n in lookup:
        if lookup[n] in a:
            # append the nth value to my results
            result.append(lookup[n])
    return result


if __name__ == "__main__":
    print(has_negatives([-1, -2, 1, 2, 3, 4, -4]))
