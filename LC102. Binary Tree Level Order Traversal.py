# 102. Binary Tree Level Order Traversal
# https://leetcode.com/problems/binary-tree-level-order-traversal/description/

'''
Given the root of a binary tree, 
return the level order traversal of its nodes' values. 
(i.e., from left to right, level by level).
'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        # time and space complexity for both approach 1 & 2 is O(n)
        '''
        # Approach 1. Recursion
        result = []
        if root == None:
            return result

        def helper(node, level):
            # level act like the index for result list 
            if len(result) == level:
                result.append([])
            
            result[level].append(node.val)

            if node.left:
                helper(node.left, level + 1)
            if node.right:
                helper(node.right, level + 1)
            
        helper(root, 0)
        return result
        '''

        # Approach 2. Iteration
        if root == None:
            return []
        
        result = []
        stack = [(root, 0)]
        
        while stack:
            curr, level = stack.pop()

            if level == len(result):
                result.append([])
            
            result[level].append(curr.val)
            
            if curr.right != None:
                stack.append((curr.right, level + 1))
            if curr.left != None:
                stack.append((curr.left, level + 1))
            
        return result

