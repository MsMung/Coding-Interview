# 270. Closest Binary Search Tree Value
# https://leetcode.com/problems/closest-binary-search-tree-value/description/
'''
Given the root of a binary search tree and a target value, 
return the value in the BST that is closest to the target.
'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def closestValue(self, root: Optional[TreeNode], target: float) -> int:
        result = None
        curr = root
        min_difference = float("inf")

        while (curr != None):
            if abs(curr.val - target) < min_difference:
                result = curr
                min_difference = abs(curr.val - target)

            if target < curr.val:
                curr = curr.left
            else:
                curr = curr.right

        return result.val
        