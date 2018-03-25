# How would you design a stack which, in addition to push and pop, has a
# function min which returns the minimum element? Push, pop, and min should all
# operate in O(1) time.


class Node(object):

    def __init__(self, value, prev, min_val):
        self.data = value
        self.prev = prev
        self.prev_min = min_val


class MinStack(object):

    def __init__(self):
        self.tail = None
        self._min = None

    def push(self, value):
        new_node = Node(value, self.tail, self._min)

        self.tail = new_node
        if self._min is None or self._min > new_node.data:
            self._min = new_node.data

    def pop(self):
        pop_val = self.tail.data

        self._min = self.tail.prev_min
        self.tail = self.tail.prev
        return pop_val

    def get_min(self):
        return self._min
