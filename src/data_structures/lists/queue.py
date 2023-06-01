from stack import Stack

# Using a stack to implement a queue, because
# our linked list doesn't have a tail pointer,
# thus doesn't support O(1) time for adding at the end


class Queue:
    def __init__(self):
        self.stack = Stack()
        self.helper_stack = Stack()

    # Enqueue -> just add to the stack (O(1) time)
    def enqueue(self, key):
        self.stack.add(key)

    # Dequeue -> remove from the helper stack (O(1) time)
    # if it's not empty, otherwise move all elements
    # from the stack to the helper stack and then
    # remove from the helper stack (O(n) time)
    def dequeue(self):
        if self.isEmpty():
            return None
        if self.helper_stack.isEmpty():
            while not self.stack.isEmpty():
                self.helper_stack.add(self.stack.pop())
        return self.helper_stack.pop()

    # If both stacks are empty, then the queue is empty
    def isEmpty(self):
        return self.stack.isEmpty() and self.helper_stack.isEmpty()

    # Size of the queue is the sum of the sizes of the stacks
    def size(self):
        return self.stack.size() + self.helper_stack.size()