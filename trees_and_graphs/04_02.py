# MINIMAL TREE: Given a sorted (increasing in order) array with unique integer
# elements write an algorithm to create a binary search tree with minimal height


class Node:

    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def __repr__(self):

        return "<Node v: {} l: {} r: {} >".format(self.value, self.left, self.right)


class Tree:

    def __init__(self):
        self.root = None

    def __repr__(self):

        return "<Tree {}>".format(self.root)


def create_bst(arr):
    """Given sorted array with unique integer elements, return bst.

    binary search function
    after finding midpoint, create node
    assign midpoint nodes as l and r nodes on parent

    >>> create_bst([1, 2, 3, 4, 5, 6, 7])
        4
      2   6
    1  3 5  7

    """

    if len(arr) == 0:
        return None
    elif len(arr) == 1:
        return Node(arr[0])

    mid = len(arr) // 2
    left_half = arr[:mid]
    right_half = arr[mid + 1:]

    current_node = Node(arr[mid])

    current_node.left = create_bst(left_half)
    current_node.right = create_bst(right_half)

    return current_node


def create_minimal_tree(arr):
    """Given an array, return a binary search tree of minimal height."""

    tree = Tree()
    tree.root = create_bst(arr)

    return tree
