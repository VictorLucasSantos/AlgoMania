# Busca em Profundidade (Deep First Search - DFS)

## O que é DFS?
A Busca em Profundidade (**DFS - Deep First Search**) é um algoritmo de busca utilizado para percorrer ou buscar elementos em estruturas de dados como **árvores** e **grafos**. O DFS explora o máximo possível cada ramo antes de retroceder.

## Funcionamento do DFS
DFS segue o conceito **LIFO (Last In, First Out)**, geralmente implementado utilizando **recursão** ou uma **pilha explícita**. O fluxo básico do algoritmo é:
1. Começar a busca de um nó inicial.
2. Marcar o nó como visitado.
3. Percorrer recursivamente (ou iterativamente) os vizinhos do nó.
4. Se encontrar o valor desejado, a busca para.
5. Se um caminho não levar ao objetivo, retrocede e explora outras opções.

## Implementação em Python
Abaixo, temos duas implementações do DFS:
- **DFS para árvores**
- **DFS para matrizes (como um labirinto)**

### 1. DFS em Árvore Binária
```python
class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def simple_deep_first_search(node, value_to_find):
    if not node:
        return False
    if node.value == value_to_find:
        return True
    return simple_deep_first_search(node.left, value_to_find) or \
           simple_deep_first_search(node.right, value_to_find)
```
#### Explicação:
- Se o nó atual for **None**, retorna `False`.
- Se o valor do nó for o que buscamos, retorna `True`.
- Recursivamente busca primeiro na **esquerda**, depois na **direita**.

### 2. DFS em uma Matriz (Labirinto)
```python
maze = []

def find_next_position(position, visited_positions):
    return 0, 0  # Implementação fictícia

def item_value(position):
    return maze[position[0]][position[1]]

def deep_first_search(position, visited_positions, value_to_find):
    if item_value(position) == value_to_find:
        return True
    next_position = find_next_position(position, visited_positions)
    if next_position:
        return deep_first_search(
            next_position, visited_positions + [position], value_to_find
        )
```
#### Explicação:
- **`item_value`**: Obtém o valor da posição atual na matriz.
- **`find_next_position`**: Retorna a próxima posição a ser explorada.
- **`deep_first_search`**:
  - Verifica se a posição atual contém o valor procurado.
  - Chama recursivamente a função para explorar a próxima posição disponível.
  
## Quando Usar DFS?
- Quando o espaço de busca for **grande** e o caminho certo pode estar **profundamente aninhado**.
- Quando a **memória é limitada** e queremos evitar o uso excessivo de espaço (DFS consome menos memória que BFS).
- Para resolver **labirintos**, **sudoku**, **detecção de ciclos** em grafos, entre outros.

## Complexidade do DFS
| Caso       | Complexidade |
|-----------|-------------|
| Melhor caso (encontra rapidamente) | O(1) |
| Pior caso (percorre tudo) | O(N) |
| Espaço (recursivo) | O(N) |

---
Essa foi uma visão geral sobre **DFS**! 🚀

