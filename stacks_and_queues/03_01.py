# THREE IN ONE: describe how you could use a single array to implement three
# stacks


class TripleStack:

    def __init__(self):
        self.array = []
        self.a_len = 0
        self.b_len = 0
        self.c_len = 0

    def __repr__(self):

        return '<TripleStack {}>'.format(self.array)

    def push_stack(self, stack, value):
        """Add value to the end of specified stack.

        >>> t_stack = TripleStack()
        >>> t_stack.push_stack('b', 'b3')
        >>> print(t_stack)
        <TripleStack ['b3']>
        >>> t_stack.push_stack('a', 'a9')
        >>> print(t_stack)
        <TripleStack ['a9', 'b3']>
        >>> t_stack.push_stack('c', 'c4')
        >>> print(t_stack)
        <TripleStack ['a9', 'b3', 'c4']>

        """

        if stack.lower() == 'a':
            self.array.insert(self.a_len, value)
            self.a_len += 1

        elif stack.lower() == 'b':
            self.array.insert(self.a_len + self.b_len, value)
            self.b_len += 1

        else:
            self.array.append(value)
            self.c_len += 1

    def pop_stack(self, stack):
        """Return and remove value from end of specified stack.

        >>> t_stack = TripleStack()
        >>> t_stack.push_stack('b', 'b3')
        >>> t_stack.push_stack('a', 'a9')
        >>> t_stack.push_stack('c', 'c4')
        >>> t_stack.push_stack('a', 'a6')
        >>> print(t_stack)
        <TripleStack ['a9', 'a6', 'b3', 'c4']>
        >>> t_stack.pop_stack('b')
        'b3'
        >>> t_stack.pop_stack('a')
        'a6'
        >>> t_stack.pop_stack('c')
        'c4'
        >>> t_stack.pop_stack('a')
        'a9'
        >>> t_stack.pop_stack('b')


        """

        value = None

        if stack.lower() == 'a' and self.a_len > 0:
            value = self.array.pop(self.a_len - 1)
            self.a_len -= 1

        elif stack.lower() == 'b' and self.b_len > 0:
            value = self.array.pop(self.a_len + self.b_len - 1)
            self.b_len -= 1

        elif stack.lower() == 'c' and self.c_len > 0:
            value = self.array.pop()
            self.c_len -= 1

        return value

    def peek_stack(self, stack):
        """Return value at the end of specified stack.

        >>> t_stack = TripleStack()
        >>> t_stack.push_stack('b', 'b3')
        >>> t_stack.push_stack('a', 'a9')
        >>> t_stack.push_stack('c', 'c4')
        >>> t_stack.push_stack('a', 'a6')
        >>> t_stack.peek_stack('b')
        b3
        >>> t_stack.peek_stack('a')
        a6
        >>> t_stack.peek_stack('c')
        c4
        >>> t_stack.peek_stack('b')
        b3

        """

        value = None

        if stack.lower() == 'a' and self.a_len > 0:
            value = self.array[self.a_len - 1]

        elif stack.lower() == 'b' and self.b_len > 0:
            value = self.array[self.a_len + self.b_len - 1]

        elif stack.lower() == 'c' and self.c_len > 0:
            value = self.array[-1]

        print(value)
