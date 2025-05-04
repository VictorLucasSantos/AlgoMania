import unittest


class Queue:
    def __init__(self):
        self._data = []

    def enqueue(self, value):
        self._data.append(value)  # Insere o item da fila

    def dequeue(self):
        if self._data:
            return self._data.pop(0)  # remove o primeiro item da fila
        raise IndexError("A fila está vazia!")

    def peek(self):
        if self._data:
            return self._data[0]  # retorna o primeiro item sem removelo
        raise IndexError("A fila está vazia!")

    def size(self):
        return len(self._data)

    def is_empty(self):
        return len(self._data) == 0


class QueueTests(unittest.TestCase):
    def setUp(self):
        self.queue = Queue()  # Corrigido

    def test_enqueue(self):
        self.queue.enqueue(10)
        self.assertEqual(self.queue.peek(), 10)

    def test_dequeue(self):
        self.queue.enqueue(1)
        self.queue.enqueue(2)
        val = self.queue.dequeue()
        self.assertEqual(val, 1)
        self.assertEqual(self.queue.peek(), 2)

    def test_is_empty(self):
        self.assertTrue(self.queue.is_empty())
        self.queue.enqueue(5)
        self.assertFalse(self.queue.is_empty())

    def test_size(self):
        self.assertEqual(self.queue.size(), 0)
        self.queue.enqueue("x")
        self.queue.enqueue("y")
        self.assertEqual(self.queue.size(), 2)

    def test_peek_empty(self):
        with self.assertRaises(IndexError):
            self.queue.peek()

    def test_dequeue_empty(self):
        with self.assertRaises(IndexError):
            self.queue.dequeue()


if __name__ == "__main__":
    unittest.main()
