class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

    def __repr__(self):
        return str(self.value)


class LinkedList:
    def __init__(self):
        self.head = None

    def __str__(self):
        cur_head = self.head
        out_string = ""
        while cur_head:
            out_string += str(cur_head.value) + " -> "
            cur_head = cur_head.next
        return out_string

    def append(self, value):
        if self.head is None:
            self.head = Node(value)
            return

        node = self.head
        while node.next:
            node = node.next

        node.next = Node(value)

    def size(self):
        size = 0
        node = self.head
        while node:
            size += 1
            node = node.next

        return size


def union(llist_1, llist_2):
    common_values = set()
    current = llist_1.head
    union_llist = LinkedList()

    while current:
        common_values.add(current.value)

        current = current.next

    current = llist_2.head

    while current:
        common_values.add(current.value)

        current = current.next

    for value in common_values:
        union_llist.append(value)

    return union_llist


def intersection(llist_1, llist_2):
    llist_1_values = set()
    current = llist_1.head
    intersection_llist = LinkedList()

    while current:
        llist_1_values.add(current.value)

        current = current.next

    current = llist_2.head

    while current:
        if current.value in llist_1_values:
            intersection_llist.append(current.value)
            llist_1_values.discard(current.value)

        current = current.next

    return intersection_llist


def test1():
    linked_list_1 = LinkedList()
    linked_list_2 = LinkedList()

    element_1 = [3, 2, 4, 35, 6, 65, 6, 4, 3, 21]
    element_2 = [6, 32, 4, 9, 6, 1, 11, 21, 1]

    for i in element_1:
        linked_list_1.append(i)

    for i in element_2:
        linked_list_2.append(i)

    print("==========")
    print(union(linked_list_1, linked_list_2))
    # 32 -> 65 -> 2 -> 35 -> 4 -> 6 -> 1 -> 9 -> 11 -> 3 -> 21 ->
    print(intersection(linked_list_1, linked_list_2))
    # 6 -> 4 -> 21 ->


def test2():
    linked_list_1 = LinkedList()
    linked_list_2 = LinkedList()

    element_1 = [3, 2, 4, 35, 6, 65, 6, 4, 3, 23]
    element_2 = [1, 7, 8, 9, 11, 21, 1]

    for i in element_1:
        linked_list_1.append(i)

    for i in element_2:
        linked_list_2.append(i)

    print("==========")
    print(union(linked_list_1, linked_list_2))
    # 65 -> 2 -> 35 -> 4 -> 6 -> 1 -> 8 -> 9 -> 7 -> 11 -> 3 -> 21 -> 23 ->
    print(intersection(linked_list_1, linked_list_2))
    # (empty)


def test3():
    linked_list_1 = LinkedList()
    linked_list_2 = LinkedList()

    element_1 = [3, 2, 4]
    element_2 = []

    for i in element_1:
        linked_list_1.append(i)

    for i in element_2:
        linked_list_2.append(i)

    print("==========")
    print(union(linked_list_1, linked_list_2))
    # 2 -> 3 -> 4 ->
    print(intersection(linked_list_1, linked_list_2))
    # (empty)


test1()
test2()
test3()
