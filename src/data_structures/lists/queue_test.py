import unittest

from queue import Queue


class QueueTest(unittest.TestCase):
    def setUp(self):
        self.queue = Queue()

    def test_dequeue_empty_list(self):
        self.assertIsNone(self.queue.dequeue())

    def test_enqueue_and_dequeue(self):
        self.queue.enqueue(1)
        self.queue.enqueue(2)
        self.queue.enqueue(3)

        self.assertEqual(self.queue.dequeue(), 1)
        self.assertEqual(self.queue.dequeue(), 2)
        self.assertEqual(self.queue.dequeue(), 3)
        self.assertIsNone(self.queue.dequeue())

    def test_isEmpty(self):
        self.assertTrue(self.queue.isEmpty())

        self.queue.enqueue(1)
        self.assertFalse(self.queue.isEmpty())

        self.queue.dequeue()
        self.assertTrue(self.queue.isEmpty())

    def test_size(self):
        self.assertEqual(self.queue.size(), 0)

        self.queue.enqueue(1)
        self.queue.enqueue(2)
        self.queue.enqueue(3)
        self.assertEqual(self.queue.size(), 3)

        self.queue.dequeue()
        self.assertEqual(self.queue.size(), 2)

        self.queue.dequeue()
        self.assertEqual(self.queue.size(), 1)

        self.queue.dequeue()
        self.assertEqual(self.queue.size(), 0)