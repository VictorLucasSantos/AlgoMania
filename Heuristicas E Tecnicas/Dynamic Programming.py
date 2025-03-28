from unittest import TestCase


# Implementação de fibonacci padrão complexidade é O(2^n)
def fibonacci(n):
    if n == 1 or n == 2:
        return 1
    return fibonacci(n - 1) + fibonacci(n - 2)


# complexidade desse algoritmo é O(n)
def fibonacci_mem(n, mem={}):
    if n == 1 or n == 2:
        return 1
    if n not in mem:
        mem[n] = fibonacci_mem(n - 1) + fibonacci_mem(n - 2)
    return mem[n]


print(fibonacci_mem(10))
print(fibonacci(10))


class MyTest(TestCase):
    def test_example_checks(self):
        self.assertEqual(1, fibonacci(1))
        self.assertEqual(2, fibonacci(2))

    def test_other_checks(self):
        self.assertEqual(1, fibonacci(1))
        self.assertEqual(2, fibonacci(4))
        self.assertEqual(3, fibonacci(4))
        self.assertEqual(5, fibonacci(5))
        self.assertEqual(8, fibonacci(6))

    def test_slow_tests(self):
        self.assertEqual(9227465, fibonacci(35))

    def test_stack_overflow_tests(self):
        self.assertEqual(9227465, fibonacci(3529))
