# Given a singly linked list, return the element k items from the end


def k_to_last(l_list, k):
    """Finds the kth element from the end of the linked list."""

    current = l_list.head
    k_pointer = l_list.head

    for _ in range(k):
        if k_pointer is None:
            return None
        k_pointer = k_pointer.next

    while k_pointer is not None:
        current = current.next
        k_pointer = k_pointer.next

    return current.data