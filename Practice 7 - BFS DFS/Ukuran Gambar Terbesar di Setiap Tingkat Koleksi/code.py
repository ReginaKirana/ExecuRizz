import sys

def tree(tokens):
    if not tokens or tokens[0] == 'null':
        return None
    from collections import deque
    class Node:
        def __init__(self, val):
            self.val = int(val)
            self.left = None
            self.right = None
    it = iter(tokens)
    root = Node(next(it))
    queue = deque([root])
    for tok in it:
        parent = queue.popleft()
        # left child
        if tok != 'null':
            parent.left = Node(tok)
            queue.append(parent.left)
        # right child if available
        try:
            tok2 = next(it)
        except StopIteration:
            break
        if tok2 != 'null':
            parent.right = Node(tok2)
            queue.append(parent.right)
    return root


def largest_values(root):
    from collections import deque
    if not root:
        return []
    result = []
    queue = deque([root])
    while queue:
        level_size = len(queue)
        level_max = -2**31
        for _ in range(level_size):
            node = queue.popleft()
            if node.val > level_max:
                level_max = node.val
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        result.append(level_max)
    return result


data = sys.stdin.read().strip().split()
if not data:
    sys.exit(0)
n = int(data[0])
tokens = data[1:1+n]

root = tree(tokens)
res = largest_values(root)
print(' '.join(str(x) for x in res))