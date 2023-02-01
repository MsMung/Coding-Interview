# 250. Count Univalue Subtrees
# https://leetcode.com/problems/count-univalue-subtrees/description/

'''
Given the root of a binary tree, 
return the number of uni-value subtrees.

A uni-value subtree means all nodes of the subtree 
have the same value.
'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countUnivalSubtrees(self, root: Optional[TreeNode]) -> int:
        # postorder traversal
        if root == None:
            return 0
        self.count = 0
        self.dfs(root)
        return self.count
        
    def dfs(self, root):
        if root.left == None and root.right == None:
            self.count += 1
            return True

        if root.left == None and root.right != None:
            right = self.dfs(root.right)
            if root.val == root.right.val and right:
                self.count += 1
                return True
        
        if root.right == None and root.left != None:
            left = self.dfs(root.left)
            if root.val == root.left.val and left:
                self.count += 1
                return True
        
        if root.right != None and root.left != None:
            left = self.dfs(root.left)
            right = self.dfs(root.right)
            if root.val == root.left.val and root.val == root.right.val and left and right:
                self.count += 1
                return True

        return False
