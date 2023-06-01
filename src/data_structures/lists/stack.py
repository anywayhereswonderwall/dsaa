from linked_list import LinkedList
# Just using the LinkedList class to implement a Stack
# as we implemented a LinkedList to have all the methods
# needed for a Stack
class Stack:
    def __init__(self):
        self.list = LinkedList()

    def add(self, key):
        self.list.addleft(key)

    def pop(self):
        return self.list.popleft()

    def size(self):
        return self.list.size()

    def isEmpty(self):
        return self.list.isEmpty()