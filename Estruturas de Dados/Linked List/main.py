class Node:
    def __init__(self, value):
        self.next = None
        self.prev = None
        self.value = value


class LinkedList:
    def __init__(self):  # Inicializa a classe vazia
        self.head = None
        self.tail = None

    def is_empty(self):  # Valida se existe o primeiro item
        return self.head is None

    def get_tail(self):
        return self.tail

    def get_head(self):
        return self.head

    def insert_node_to_tail(self, node):
        if self.is_empty():  # Se estiver vazia o nó é o começo e o fim
            self.head = node
            self.tail = node
        else:
            # Conecta o novo nó com o fim da lista
            self.tail.next = node
            node.prev = self.tail
            self.tail = node  # Atualiza o fim da lista

    def insert_node_to_head(self, node):
        if self.is_empty():  # Se estiver vazia o nó é o começo e o fim
            self.head = node
            self.tail = node
        else:
            # Conecta o novo nó com o início da lista
            node.next = self.head
            self.head.prev = node
            self.head = node  # Atualiza o início da lista

    def print_list(self):
        current = self.head
        while current:
            print(current.value, end=" <-> ")
            current = current.next
        print("None")


ll = LinkedList()
ll.insert_node_to_tail(Node(1))
ll.insert_node_to_tail(Node(2))
ll.insert_node_to_head(Node(0))
ll.print_list()
# 0 <-> 1 <-> 2 <-> None
