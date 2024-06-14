import unittest
import collections

class Queue:
    def __init__(self):
        self._data = collections.deque()
        """Realiza a inserção de valores na lista de Queue
        """
    def enqueue(self, value):
        self._data.append(value)
        
    """Remove o primeiro elemento da Queue"""
    def dequeue(self):
        self._data.popleft()

class QueueTests(unittest.TestCase):
    def setUp(self) -> None:
        if self._data:
            self.queue = Queue()
        
    def test_simple(self):
        self.queue.enqueue(1)
        
    def test_empty_queue(self):
        self.queue.dequeue()