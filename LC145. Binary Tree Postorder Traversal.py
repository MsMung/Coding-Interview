# 145. Binary Tree Postorder Traversal
# https://leetcode.com/problems/binary-tree-postorder-traversal/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        '''
        # Approach 1. Recursion
        result = []
        def helper(root):
            if root != None:
                helper(root.left)
                helper(root.right)
                result.append(root.val)
        helper(root)
        return result
        '''

        # Approach 2. Iteration
        # version 1
        result = []
        if root == None:
            return result

        stack = [root]

        while len(stack) != 0:
            curr = stack.pop()
            # insert add the beginning of the list each time,
            # the root will be shifted to the end
            result.insert(0, curr.val)
            if (curr.left != None):
                stack.append(curr.left)
            if (curr.right != None):
                stack.append(curr.right)

        return result

        # approach 2
        result = []
        stack = []
        curr = root

        while stack or curr != None:
            if curr != None:
                stack.append(curr)
                result.insert(0, curr.val)
                curr = curr.right
            else:
                node = stack.pop()
                curr = node.left
        
        return result
