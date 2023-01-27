# 450. Delete Node in a BST
# https://leetcode.com/problems/delete-node-in-a-bst/description/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def findNode(self, root, key):
        parent = None
        curr = root
        while (curr != None and curr.val != key):
            parent = curr
            if key < curr.val:
                curr = curr.left
            else:
                curr = curr.right
        if curr == None:
            parent = None
        return (curr, parent)
    
    def findSmallest(self, root):
        parent = None
        curr = root
        while curr.left != None:
            parent = curr
            curr = curr.left

        return (curr, parent)

    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        (delete_node, delete_parent) = self.findNode(root, key)

        if delete_node == None:
            return root

        # if delete_node has no left child
        if delete_node.left == None:
            if delete_parent == None:
                root = delete_node.right
            elif delete_parent.left == delete_node:
                delete_parent.left = delete_node.right
            else:
                delete_parent.right = delete_node.right

        # if delete_node has no right child
        elif delete_node.right == None:
            if delete_parent == None:
                root = delete_node.left
            elif delete_parent.left == delete_node:
                delete_parent.left = delete_node.left
            else:
                delete_parent.right = delete_node.left

        # if delete_node has both left and right child
        else:
            # find the next bigger node 
            (next_bigger, next_parent) = self.findSmallest(delete_node.right)
            delete_node.val = next_bigger.val
            # delete next_bigger
            if next_parent == None:
                delete_node.right = next_bigger.right
            else:
                next_parent.left = next_bigger.right
        
        return root
