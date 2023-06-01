from linked_list_node import Node

# Implementing generics
from typing import TypeVar, Generic
T = TypeVar('T')


class LinkedList(Generic[T]):
    def __init__(self) -> None:
        # Using dummy node to avoid edge cases when adding
        # and removing elements
        self.head = Node(None)
        self.n = 0

    # Pop removes last element and returns it
    def pop(self) -> T:
        # Since we don't use tail pointer nor previous pointers
        # we need to find last element in O(n)

        # Nothing to pop if is empty
        if self.isEmpty():
            return None

        # Find last but one element, because we have to break its link to the last element
        last_but_one = self.head
        while last_but_one.next.next:
            last_but_one = last_but_one.next
        # At this point last_but_one stores reference to n - 1 element
        # we get last element's value by accessing last_but_one.next.key and save it to return later
        key_to_return = last_but_one.next.key

        # Breaking last link and allowing garbage collector to remove it from memory
        last_but_one.next = None

        # Decrease size by one
        self.n -= 1

        # Returning key of just removed node
        return key_to_return

    def popleft(self) -> T:
        # We have instant access to first element from left (by head pointer), thus popleft
        # will run in O(1) time

        # Nothing to pop if is empty
        if self.isEmpty():
            return None

        # First node from left
        key_to_return = self.head.next.key

        # Shifting the pointer of head (dummy node) to the second element
        self.head.next = self.head.next.next

        # Decrease size by one
        self.n -= 1

        return key_to_return

    # Add element to the end of the list
    def add(self, key: T) -> None:
        last = self.head
        # Adding new node to the end of the list
        # in O(n) time

        # Getting the last element
        while last.next:
            last = last.next

        # Adding the new node after the tail
        last.next = Node(key)

        # Increment size
        self.n += 1

    def addleft(self, key: T) -> None:
        # Adding element to the beginning of the list
        # in O(1) time

        # Creating new node
        new_node = Node(key)

        # Shifting the pointer of head (dummy node) to the new node
        new_node.next = self.head.next
        self.head.next = new_node

        # Increment size
        self.n += 1

    # Check if list is empty
    def isEmpty(self) -> bool:
        return self.n == 0

    # Return size
    def size(self) -> int:
        return self.n

