# 700. Search in a Binary Search Tree
# https://leetcode.com/problems/search-in-a-binary-search-tree/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        curr = root
        while (curr != None and curr.val != val):
            if val < curr.val:
                curr = curr.left
            else:
                curr = curr.right
        
        return curr

# Leetcode official solution
# Approach 1. Recursion
# time complexity: O(H) where H is the tree height.
# that results in O(logN) in the average case
# and O(N) in the worst case

# space complexity: O(H) to keep the recursion stack
class Solution:
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        if root == None or root.val == val:
            return root
        
        if val < root.val:
            return self.searchBST(root.left, val)
        else:
            return self.searchBST(root.right, val)

# Approach 2. Iteration
# time complexity: O(H)
# space complexity: O(1)
class Solution:
    def searchBST(self, root: TreeNode, val: int) -> TreeNode:
        while root is not None and root.val != val:
            root = root.left if val < root.val else root.right
        return root