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
        # Approach 1. Recursion
        result = []

        def helper(root):
            if root != None:
                helper(root.left)
                result.append(root.val)
                helper(root.right)
        
        helper(root)
        return result

        # Approach 2. Iteration
        # time & space complexity is O(n)
        # version 1. leetcode solution
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
    
        # version 2. leetcode comment sol
        def pushAllLeft(node, stack):
            while node != None:
                stack.append(node)
                node = node.left

        result = []
        stack = []
        pushAllLeft(root, stack)
        while stack:
            curr = stack.pop()
            result.append(curr.val)
            pushAllLeft(curr.right, stack)

        return result

