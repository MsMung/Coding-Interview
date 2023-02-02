# 106. Construct Binary Tree from Inorder and Postorder Traversal
# https://leetcode.com/problems/construct-binary-tree-from-inorder-and-postorder-traversal/description/

'''
Given two integer arrays inorder and postorder 
where inorder is the inorder traversal of a binary tree 
and postorder is the postorder traversal of the same tree, 
construct and return the binary tree.

Example:
Input: inorder = [9,3,15,20,7], postorder = [9,15,7,20,3]
Output: [3,9,20,null,null,15,7]
'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        # time & space complexcity O(N) since we are storing the tree
        def helper(left, right):
            if left > right:
                return None

            root_val = postorder.pop()
            root = TreeNode(root_val)

            # Since we are popping nodes from the end from post-order list, 
            # we come across nodes in the order: 
            # node, node.right and then node.left
            root.right = helper(lookup[root_val] + 1, right)
            root.left = helper(left, lookup[root_val] - 1)
            
            return root
    
        lookup = {}
        for i in range(len(inorder)):
            lookup[inorder[i]] = i
        
        return helper(0, len(inorder) - 1)

