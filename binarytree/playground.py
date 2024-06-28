from binarytree import TreeNode
from binarytree import traverse_inorder, traverse_preorder, get_depth

from bst import build_bst, is_valid_bst
def create_tree():
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)
    root.right.left = TreeNode(6)
    root.right.right = TreeNode(7)
    return root

if __name__=="__main__":
    tree = create_tree()
    values = traverse_inorder(tree)
    bst = build_bst(values, False)
    is_bst = is_valid_bst(bst)
    inorder_values = traverse_inorder(bst)

    print(values)
    print(inorder_values)
    print(is_bst)
    print(get_depth(tree))
    print(get_depth(bst))