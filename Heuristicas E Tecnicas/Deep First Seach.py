maze = []


class Node:
    value = 0
    left = None
    right = None


def simple_deep_first_seach(node, value_to_find):
    if not node:
        return False
    if node.value == value_to_find:
        return True
    return deep_first_seach(node.left, value_to_find) or deep_first_seach(
        node.left, value_to_find
    )


def find_next_position(
    position,
):
    return 0, 0


def item_value(position):
    return maze[position[0], position[1]]


def deep_first_seach(position, visited_positions, value_to_find):
    if item_value(position) == value_to_find:
        return True

    next_position = find_next_position(position, visited_positions)
    if next_position:
        return deep_first_seach(
            next_position, visited_positions + [position], value_to_find
        )
