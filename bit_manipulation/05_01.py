# INSERTION: You are given two 32-bit numbers, N and M, and two bit positions,
# i and j. Write a method to insert M into N such that M starts at bit j and
# ends at bit i. You can assume that the bits j through i have enought space to
# fit all of M. That is, if M = 10011, you can assume that there are at least 5
# bits between j and i. You would not, for example, have j = 3 and i = 2,
# because M could not fully fit between bit 3 and bit 2.

# Example:
# Input: N = 10000000000, M = 10011, i = 2, j = 6
# Output: N = 10001001100

# hints 137, 169, 215


def insert_number(n, m, i, j):
    """
    >>> insert_number(10000000000, 10011, 2, 6)
    10001001100

    """
    n = str(n)
    m = str(m)

    n_beginning = n[:-(j + 1)]
    n_end = n[-i:]

    new_number = n_beginning + m + n_end

    return int(new_number)
