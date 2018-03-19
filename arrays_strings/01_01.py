from collections import defaultdict

# 1.1 Write a function that determines if every character in a string is unique


def is_unique(string):
    """Determines if each character in given string is unique.

    Creates an array of False values for each ASCII character. Converts each
    string character to ASCII number value and stores True value at that value
    index. If any value lookup is already True, that means the current character
    is a duplicate.

    """
    char_bool = [False] * 128

    for char in string:
        val = ord(char)
        if char_bool[val]:
            return False
        char_bool[val] = True

    return True


def is_unique_set(string):
    """Determines if each character in given string is unique.

    Converts string to a set. If length of set and string differ, then there
    were duplicates in the original string.

    """

    unique_char = set(string)

    if len(string) != len(unique_char):
        return False

    return True


def is_unique_dict(string):
    """Determines if each character in given string is unique.

    Stores counts in dictionary, compares length of keys to length of string.
    Not optimal solution.

    """

    char_ct = defaultdict(int)
    for char in string:
        char_ct[char] += 1

    if len(char_ct) != len(string):
        return False

    return True


# Extra practice: Find duplicated characters in given string.


def find_dups(string):
    """Returns the duplicated characters in a given string.

    Stores whether character was found in bool array. If a duplicate is found,
    the character is added to the dups array.

    """

    char_bool = [False] * 128
    dups = []

    for char in string:
        val = ord(char)

        if char_bool[val]:
            dups.append(char)

        char_bool[val] = True

    return dups


def find_dups_dict(string):
    """Returns the duplicated characters in a given string.

    Stores character counts in a dictionary. If count for a character is greater
    than one, that character is added to an array of dups.

    """
    char_ct = defaultdict(int)
    for char in string:
        char_ct[char] += 1

    dups = []
    for char, ct in char_ct.items():
        if ct > 1:
            dups.append(char)

    return dups
