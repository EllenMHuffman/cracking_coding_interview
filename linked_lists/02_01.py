# Remove duplicates from a linked list


def del_dups(l_list):
    """Given linked list, remove duplicates in place."""

    unique_vals = set()

    current = l_list.head

    while current is not None and current.next is not None:
        unique_vals.add(current.data)

        if current.next.data in unique_vals:
            current.next = current.next.next

        else:
            current = current.next
