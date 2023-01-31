# 112. Path Sum
# https://leetcode.com/problems/path-sum/description/

'''
Given the root of a binary tree and an integer targetSum, 
return true if the tree has a root-to-leaf path such that adding up all the values along the path equals targetSum.

A leaf is a node with no children.
'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        # time complexity O(n), visit each node once
        # space complexity O(H)
        
        # 1 recursion
        if root == None:
            return False
        
        # calculate remaining sum
        targetSum -= root.val
        if root.left == None and root.right == None:
            return targetSum == 0
        
        return self.hasPathSum(root.left, targetSum) or self.hasPathSum(root.right, targetSum)
       

        # 2 iteration using stack
        '''
        we start from a stack which contains the root node and the corresponding remaining sum which is sum - root.val. 
        Then we proceed to the iterations: pop the current node out of the stack and return True if the remaining sum is 0 and we're on the leaf node. 
        If the remaining sum is not zero or we're not on the leaf yet then we push the child nodes and corresponding remaining sums into stack.
        '''
        if root == None:
            return False

        stack = [(root, targetSum - root.val)]
        while len(stack) != 0:
            top_node, remainingSum = stack.pop()

            if top_node.left == None and top_node.right == None and remainingSum == 0:
                return True
            
            if top_node.right:
                stack.append((top_node.right, remainingSum - top_node.right.val))

            if top_node.left:
                stack.append((top_node.left, remainingSum - top_node.left.val))
        
        return False

