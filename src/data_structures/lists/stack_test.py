import unittest

from stack import Stack


class StackTest(unittest.TestCase):
    def setUp(self):
        self.stack = Stack()

    def test_pop_empty_list(self):
        self.assertIsNone(self.stack.pop())

    def test_add_and_pop(self):
        self.stack.add(1)
        self.stack.add(2)
        self.stack.add(3)

        self.assertEqual(self.stack.pop(), 3)
        self.assertEqual(self.stack.pop(), 2)
        self.assertEqual(self.stack.pop(), 1)
        self.assertIsNone(self.stack.pop())

    def test_isEmpty(self):
        self.assertTrue(self.stack.isEmpty())

        self.stack.add(1)
        self.assertFalse(self.stack.isEmpty())

        self.stack.pop()
        self.assertTrue(self.stack.isEmpty())

    def test_size(self):
        self.assertEqual(self.stack.size(), 0)

        self.stack.add(1)
        self.stack.add(2)
        self.stack.add(3)
        self.assertEqual(self.stack.size(), 3)

        self.stack.pop()
        self.assertEqual(self.stack.size(), 2)

        self.stack.pop()
        self.assertEqual(self.stack.size(), 1)

        self.stack.pop()
        self.assertEqual(self.stack.size(), 0)