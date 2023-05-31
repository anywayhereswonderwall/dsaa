class Node:
    def __init__(self, key):
        self.key = key
        # The degree
        self.degree = 0

        self.parent = None
        self.sibling = None
        self.child = None
