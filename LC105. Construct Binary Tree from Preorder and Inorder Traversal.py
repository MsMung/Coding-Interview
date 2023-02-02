# 105. Construct Binary Tree from Preorder and Inorder Traversal
# https://leetcode.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal/description/

'''
Given two integer arrays preorder and inorder 
where preorder is the preorder traversal of a binary tree 
and inorder is the inorder traversal of the same tree, 
construct and return the binary tree.

Example:
Input: preorder = [3,9,20,15,7], inorder = [9,3,15,20,7]
Output: [3,9,20,null,null,15,7]
'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        preorder_index = 0
        
        def helper(left, right):
            if left > right:
                return None

            # The nonlocal statement causes 
            # a variable definition to bind 
            # to a previously created variable 
            # in the nearest scope
            nonlocal preorder_index
            root_val = preorder[preorder_index]
            preorder_index += 1
            root = TreeNode(root_val)
            root.left = helper(left, lookup[root_val] - 1)
            root.right = helper(lookup[root_val] + 1, right)
            return root
        
        lookup = {}
        for i in range(len(inorder)):
            lookup[inorder[i]] = i
        
        return helper(0, len(inorder) - 1)
