# 94. Binary Tree Inorder Traversal
# https://leetcode.com/problems/binary-tree-inorder-traversal/description/

'''
Given the root of a binary tree, 
return the inorder traversal of its nodes' values.
'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        '''
        # Approach 1. Recursion
        result = []

        def helper(root, result):
            if root != None:
                helper(root.left, result)
                result.append(root.val)
                helper(root.right, result)
        
        helper(root, result)
        return result
        '''

        # Approach 2. Iteration
        # time & space complexity is O(n)
        result = []
        stack = []
        curr = root

        while curr != None or len(stack) != 0:
            while (curr != None):
                stack.append(curr)
                curr = curr.left
            curr = stack.pop()
            result.append(curr.val)
            curr = curr.right

        return result

