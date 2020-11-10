class Ticket:
    def __init__(self, source, destination):
        self.source = source
        self.destination = destination


def reconstruct_trip(tickets, length):
    """
    Function that takes tickets and matches 
    each destination to its respective source 
    and destination (if one exists)
    """
    lookup = {}
    # create hash table index using object sources
    for i in range(length):
        lookup[tickets[i].source] = tickets[i].destination
    
    route = [lookup['NONE']]
    # append the destinations to their appropriate locations
    while route[len(route) - 1] != 'NONE':
        route.append(lookup[route[len(route)-1]])

    return route
