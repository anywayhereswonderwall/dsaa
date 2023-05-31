
# Implementing generics
from typing import TypeVar, Generic
T = TypeVar('T')


# Using only next pointer, no previous pointer
class Node(Generic[T]):
    def __init__(self, key: T):
        self.key = key
        self.next = None