from collections import defaultdict

# Determine whether one string is a permutation of a second string.


def is_perm(str1, str2):
    """Determines if string1 is permutation of string2.

    String lengths compared for equality. Character counts for string1 are added
    to dict. Counts are decremented for string2. If any count becomes negative,
    the strings are not permutations.

    """

    if len(str1) != len(str2):
        return False

    char_ct = defaultdict(int)

    for char in str1:
        char_ct[char] += 1

    for char in str2:
        char_ct[char] -= 1

        if char_ct[char] < 0:
            return False

    return True
