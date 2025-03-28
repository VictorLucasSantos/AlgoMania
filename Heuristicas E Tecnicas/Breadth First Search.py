class Node:
    value = 0
    left = None
    right = None


def breath_first_search(root, value_to_find):
    if root:
        queue = [root]
        while queue:
            node = queue.pop(0)
            # verifica valor procurado
            if node.value == value_to_find:
                return True
            # Analisa os filhos
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)


maze = []


def find_next_possible_positions(maze, p1, p2, visited_positions):
    return 0, 0


def breadth_first_search(maze, value_to_find):
    if maze:
        queue = [(0, 0)]
        visited_positions = []
        while queue:
            p1, p2 = queue.pop(0)
            # verifica valor procurado
            if maze[p1][p2] == value_to_find:
                return True
            # Analisa os filhos
            visited_positions.append((p1, p2))
            queue += find_next_possible_positions(maze, p1, p2, visited_positions)
