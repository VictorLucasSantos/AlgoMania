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


pilha = Stack()
pilha.push(10)
pilha.push(20)
pilha.push(30)

print(pilha.peek())
print(pilha.pop())
print(pilha.peek())
print(pilha.size())
