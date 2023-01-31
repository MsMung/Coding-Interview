# 450. Delete Node in a BST
# https://leetcode.com/problems/delete-node-in-a-bst/description/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        def bst_find(root, key):
            parent = None
            curr = root

            while curr != None and curr.val != key:
                parent = curr
                if key < curr.val:
                    curr = curr.left
                else:
                    curr = curr.right
            if curr == None:
                parent = None
            return (curr, parent)
        
        
        def bst_find_smallest(root):
            parent = None
            curr = root
            while curr.left != None:
                parent = curr
                curr = curr.left
            return (curr, parent)
        
        
        # search for the node to delete
        (del_node, del_parent) = bst_find(root, key)

        # delete the node
        # the node to delete has 1 child
        if del_node != None:
            # no left child
            if del_node.left == None:
                if del_parent == None:
                    root = del_node.right
                elif del_parent.left == del_node:
                    del_parent.left = del_node.right
                else:
                    del_parent.right = del_node.right
            
            # no right child
            elif del_node.right == None:
                if del_parent == None:
                    root = del_node.left
                elif del_parent.left == del_node:
                    del_parent.left = del_node.left
                else:
                    del_parent.right = del_node.left

            # the node to delete has 2 children
            else:
                (next_bigger, next_parent) = bst_find_smallest(del_node.right)
                # copy data from next bigger node to node to delete
                del_node.val = next_bigger.val

                # delete the next bigger node
                if next_parent == None:
                    del_node.right = next_bigger.right
                else:
                    next_parent.left = next_bigger.right
            
        return root
