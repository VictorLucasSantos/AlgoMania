## O que é BFS?
A Busca em Largura (**BFS - Breadth First Search**) é outro algoritmo de busca utilizado para percorrer estruturas de dados como **árvores** e **grafos**. Ao contrário do DFS, o BFS explora os nós **nível por nível**, garantindo que todos os nós de um nível sejam visitados antes de passar para o próximo.

## Funcionamento do BFS
BFS segue o conceito **FIFO (First In, First Out)** e geralmente é implementado utilizando **filas**:
1. Começa a busca a partir de um nó inicial.
2. Adiciona esse nó à fila e marca como visitado.
3. Remove o nó da fila e adiciona seus vizinhos não visitados.
4. Repete até encontrar o valor desejado ou a fila estar vazia.

### Implementação do BFS em Python
```python
from collections import deque

def breadth_first_search(start_node, value_to_find):
    queue = deque([start_node])
    visited = set()
    
    while queue:
        node = queue.popleft()
        if node.value == value_to_find:
            return True
        visited.add(node)
        
        for neighbor in (node.left, node.right):
            if neighbor and neighbor not in visited:
                queue.append(neighbor)
    
    return False
```

### Comparação DFS vs BFS
| Algoritmo | Melhor para |
|-----------|-------------|
| **DFS** | Espaços grandes e buscas profundas |
| **BFS** | Encontrar caminhos mais curtos |

---
Essa foi uma visão geral sobre **DFS e BFS**! 🚀

