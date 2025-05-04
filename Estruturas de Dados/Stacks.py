class Stack:
    def __init__(self):
        self.itens = []

    def push(self, item):
        self.itens.append(item)

    def pop(self):
        if not self.is_empty():
            return self.itens.pop()
        raise IndexError("A lista está vazia!")

    def peek(self):
        if not self.is_empty():
            return self.itens[-1]
        return None

    def is_empty(self):
        return len(self.itens) == 0

    def size(self):
        return len(self.itens)


import unittest


class StackTests(unittest.TestCase):
    def setUp(self):
        self.stack = Stack()

    def test_push_and_peek(self):
        self.stack.push(10)
        self.assertEqual(self.stack.peek(), 10)

        self.stack.push(20)
        self.assertEqual(self.stack.peek(), 20)

    def test_pop(self):
        self.stack.push(1)
        self.stack.push(2)
        self.assertEqual(self.stack.pop(), 2)  # LIFO
        self.assertEqual(self.stack.pop(), 1)

    def test_pop_empty(self):
        with self.assertRaises(IndexError):
            self.stack.pop()

    def test_peek_empty(self):
        self.assertIsNone(self.stack.peek())

    def test_is_empty_and_size(self):
        self.assertTrue(self.stack.is_empty())
        self.assertEqual(self.stack.size(), 0)

        self.stack.push(5)
        self.assertFalse(self.stack.is_empty())
        self.assertEqual(self.stack.size(), 1)

        self.stack.push(10)
        self.assertEqual(self.stack.size(), 2)
        self.stack.pop()
        self.assertEqual(self.stack.size(), 1)


if __name__ == "__main__":
    unittest.main()
