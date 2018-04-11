# ROUTE BETWEEN NODES: Given a directed graph, design an algorithm to find out
# whether there is a route between two nodes


def has_route(graph, node_a, node_b):
    """Return whether two given nodes on given graph are connected.

    graph is a dictionary

    >>> g = {'ellen': ['erik', 'olivia'], 'erik': ['dan', 'olivia', 'ellen'], 'jane': ['bob']}
    >>> has_route(g, 'ellen', 'erik')
    True
    >>> has_route(g, 'ellen', 'dan')
    True
    >>> has_route(g, 'ellen', 'jane')
    False

    """

    elements = list(graph[node_a])

    seen = set()

    while elements:

        element = elements.pop()

        if element == node_b:
            return True

        seen.add(element)

        try:
            for new_element in graph[element]:
                if new_element not in seen:
                    elements.append(new_element)
        except KeyError:
            continue

    return False
