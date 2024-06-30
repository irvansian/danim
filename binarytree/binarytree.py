class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def traverse_preorder(root):
    values = []

    def dfs(node):
        if not node:
            return

        values.append(node.val)
        dfs(node.left)
        dfs(node.right)

    dfs(root)
    return values


def traverse_inorder(root):
    values = []

    def dfs(node):
        if not node:
            return

        dfs(node.left)
        values.append(node.val)
        dfs(node.right)

    dfs(root)
    return values


def traverse_postorder(node):
    if not node:
        return

    traverse_postorder(node.left)
    traverse_postorder(node.right)
    print(node.val)


def is_balanced(root):
    def balanced(node):
        if not node:
            return True, 0

        left_balanced, left_depth = is_balanced(node.left)
        right_balanced, right_depth = is_balanced(node.right)

        return ((left_balanced and right_balanced
                 and abs(left_depth - right_depth) <= 1),
                max(left_depth, right_depth) + 1)

    return balanced(root)[0]


def same_tree(node1, node2):
    if not node1 and not node2:
        return True

    if not node1 or not node2 or node1.val != node2.val:
        return False

    if not same_tree(node1.left, node2.left):
        return False
    if not same_tree(node1.right, node2.right):
        return False
    return True


def get_depth(root):
    max_depth = [0]

    def dfs(node, depth):
        if not node:
            return

        if not node.left and not node.right:
            max_depth[0] = max(max_depth[0], depth)
            return

        dfs(node.left, depth + 1)
        dfs(node.right, depth + 1)

    dfs(root, 1)
    return max_depth[0]


def is_mirrored(node1, node2):
    return (same_tree(node1.left, node2.right) and
            same_tree(node1.right, node2.left))


def lowest_common_ancestor(root, val1, val2):
    if not root:
        return None

    if root.val == val1 or root.val == val2:
        return root

    left = lowest_common_ancestor(root.left, val1, val2)
    right = lowest_common_ancestor(root.right, val1, val2)

    if left and right:
        return root
    else:
        if left and find_node(root.left, [val1, val2]):
            return left

        if right and find_node(root.right, [val1, val2]):
            return right

        return None


def find_node(node, values):
    if not node:
        return

    if node.val in values:
        return True

    if find_node(node.left, values):
        return True

    if find_node(node.right, values):
        return True

    return False
