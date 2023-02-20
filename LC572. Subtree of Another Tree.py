# 572. Subtree of Another Tree
# https://leetcode.com/problems/subtree-of-another-tree/description/
'''
Given the roots of two binary trees root and subRoot, 
return true if there is a subtree of root 
with the same structure and node values of subRoot 
and false otherwise.

A subtree of a binary tree tree is a tree 
that consists of a node in tree 
and all of this node's descendants. 
The tree tree could also be considered as 
a subtree of itself.
'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p, q):
            if p == None and q == None:
                return True

            if p == None or q == None:
                return False

            if p.val == q.val:
                return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)

    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if root == None and subRoot == None:
            return True

        if root == None or subRoot == None:
            return False

        stack = [root]
        while stack:
            top_node = stack.pop()
            if top_node != None:
                if top_node.val == subRoot.val and self.isSameTree(top_node, subRoot):
                    return True
                
                stack.append(top_node.left)
                stack.append(top_node.right)

        return False

