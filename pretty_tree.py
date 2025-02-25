from collections import deque

class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

def build_tree(arr):
    """Builds a binary tree from a breadth-first list representation,
    where None indicates a missing node."""
    if not arr:
        return None
    root = Node(arr[0])
    queue = deque([root])
    i = 1
    while queue and i < len(arr):
        node = queue.popleft()
        # Process left child
        if i < len(arr):
            if arr[i] is not None:
                node.left = Node(arr[i])
                queue.append(node.left)
            i += 1
        # Process right child
        if i < len(arr):
            if arr[i] is not None:
                node.right = Node(arr[i])
                queue.append(node.right)
            i += 1
    return root

def display(root):
    """Prints the tree with the root at the top."""
    lines, *_ = _display_aux(root)
    for line in lines:
        print(line)

def _display_aux(node):
    """
    Returns a list of strings, the width, height, and horizontal coordinate of the root.
    This function recursively builds the string representation for a tree.
    """
    # No child.
    if node.right is None and node.left is None:
        line = str(node.val)
        width = len(line)
        height = 1
        middle = width // 2
        return [line], width, height, middle

    # Only left child.
    if node.right is None:
        lines, n, p, x = _display_aux(node.left)
        s = str(node.val)
        u = len(s)
        first_line = (x + 1) * " " + (n - x - 1) * "_" + s
        second_line = x * " " + "/" + (n - x - 1 + u) * " "
        shifted_lines = [line + u * " " for line in lines]
        return [first_line, second_line] + shifted_lines, n + u, p + 2, n + u // 2

    # Only right child.
    if node.left is None:
        lines, n, p, x = _display_aux(node.right)
        s = str(node.val)
        u = len(s)
        first_line = s + x * "_" + (n - x) * " "
        second_line = (u + x) * " " + "\\" + (n - x - 1) * " "
        shifted_lines = [u * " " + line for line in lines]
        return [first_line, second_line] + shifted_lines, n + u, p + 2, u // 2

    # Two children.
    left, n, p, x = _display_aux(node.left)
    right, m, q, y = _display_aux(node.right)
    s = str(node.val)
    u = len(s)
    first_line = (x + 1) * " " + (n - x - 1) * "_" + s + y * "_" + (m - y) * " "
    second_line = x * " " + "/" + (n - x - 1 + u + y) * " " + "\\" + (m - y - 1) * " "
    if p < q:
        left += [" " * n] * (q - p)
    elif q < p:
        right += [" " * m] * (p - q)
    zipped_lines = zip(left, right)
    lines = [first_line, second_line] + [a + u * " " + b for a, b in zipped_lines]
    return lines, n + m + u, max(p, q) + 2, n + u // 2

# Example usage:
if __name__ == '__main__':
    tree_arr = [-9, -3, 2, None, 4, 4, 0, -6, None, -5]
    root = build_tree(tree_arr)
    display(root)
