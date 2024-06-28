from binarytree import TreeNode
from binarytree import traverse_inorder


def is_valid_bst(root):
    def valid(node, left, right):
        if not node:
            return True

        if not (left < node.val < right):
            return False

        if not valid(node.left, left, node.val):
            return False

        if not valid(node.right, node.val, right):
            return False
        return True

    return valid(root, float('-inf'), float('inf'))


def build_bst(unsorted_list, is_sorted):
    sorted_list = unsorted_list if is_sorted else sorted(unsorted_list)

    def build_tree(left, right):
        if left == right:
            return TreeNode(sorted_list[left], None, None)

        mid = (left + right) // 2
        left_tree = build_tree(left, mid - 1)
        right_tree = build_tree(mid + 1, right)
        node = TreeNode(sorted_list[mid], left_tree, right_tree)
        return node

    return build_tree(0, len(sorted_list) - 1)


def insert(root, val):
    if not root:
        return TreeNode(val=val, left=None, right=None)

    if val < root.val:
        root.left = insert(root.left, val)
    elif val > root.val:
        root.right = insert(root.right, val)
    return root


def delete_node(root, val):
    if not root:
        return root

    if val < root.val:
        root.left = delete_node(root.left, val)
    elif val > root.val:
        root.right = delete_node(root.root, val)
    else:
        if not root.left:
            return root.right
        if not root.right:
            return root.left

        cur = root.right
        while cur.left:
            cur = cur.left
        root.val = cur.val
        root.right = delete_node(root.right, cur.val)
    return root



def balance_bst(root):
    values = traverse_inorder(root)
    tree = build_bst(values, True)
    return tree