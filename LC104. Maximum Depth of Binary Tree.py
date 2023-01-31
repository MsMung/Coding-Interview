# 104. Maximum Depth of Binary Tree
# https://leetcode.com/problems/maximum-depth-of-binary-tree/

'''
Given the root of a binary tree, return its maximum depth.

A binary tree's maximum depth is the number of nodes 
along the longest path from the root node down to 
the farthest leaf node.
'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        # time complexity O(n): visit each node once
        # space complexity O(H):
        # worstcase O(H) is O(n), average case O(H) is O(logn)
        '''
        # approach 1. recursion
        if root == None:
            return 0
        
        left_max = self.maxDepth(root.left)
        right_max = self.maxDepth(root.right)

        return max(left_max, right_max) + 1
        
       
        # approach 2. DFS
        def dfs(root):
            if root == None:
                return 0
            
            return max(dfs(root.left), dfs(root.right)) + 1
        
        return dfs(root)
        '''

        # approach 3. iteration
        if root == None:
            return 0

        result = 0
        stack = [(root, 1)]
        while len(stack) != 0:
            top_node, depth = stack.pop()
            if top_node != None:
                result = max(result, depth)
                stack.append((top_node.right, depth + 1))
                stack.append((top_node.left, depth + 1))
        
        return result
    