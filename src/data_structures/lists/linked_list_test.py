import unittest

from linked_list import LinkedList


class LinkedListTest(unittest.TestCase):
    def setUp(self):
        self.linked_list = LinkedList()

    def test_pop_empty_list(self):
        self.assertIsNone(self.linked_list.pop())

    def test_popleft_empty_list(self):
        self.assertIsNone(self.linked_list.popleft())

    def test_add_and_pop(self):
        self.linked_list.add(1)
        self.linked_list.add(2)
        self.linked_list.add(3)

        self.assertEqual(self.linked_list.pop(), 3)
        self.assertEqual(self.linked_list.pop(), 2)
        self.assertEqual(self.linked_list.pop(), 1)
        self.assertIsNone(self.linked_list.pop())

    def test_add_and_popleft(self):
        self.linked_list.add(1)
        self.linked_list.add(2)
        self.linked_list.add(3)

        self.assertEqual(self.linked_list.popleft(), 1)
        self.assertEqual(self.linked_list.popleft(), 2)
        self.assertEqual(self.linked_list.popleft(), 3)
        self.assertIsNone(self.linked_list.popleft())

    def test_isEmpty(self):
        self.assertTrue(self.linked_list.isEmpty())

        self.linked_list.add(1)
        self.assertFalse(self.linked_list.isEmpty())

        self.linked_list.pop()
        self.assertTrue(self.linked_list.isEmpty())

    def test_size(self):
        self.assertEqual(self.linked_list.size(), 0)

        self.linked_list.add(1)
        self.linked_list.add(2)
        self.linked_list.add(3)
        self.assertEqual(self.linked_list.size(), 3)

        self.linked_list.pop()
        self.assertEqual(self.linked_list.size(), 2)

        self.linked_list.popleft()
        self.assertEqual(self.linked_list.size(), 1)

        self.linked_list.pop()
        self.assertEqual(self.linked_list.size(), 0)


if __name__ == '__main__':
    unittest.main()
