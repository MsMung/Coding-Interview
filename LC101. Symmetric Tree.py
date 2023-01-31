# 101. Symmetric Tree
# https://leetcode.com/problems/symmetric-tree/description/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        
        # approach 1. recursion
        # time complexity O(N), traverse the tree once
        # space complexity O(H), H is the height of the tree

        # the tree is symmetric iff:
        # 1. left.val == right.val
        # 2. isMirror(left.left, right.right)
        # and isMirror(left.right, right.left)
        def isMirror(left, right):
            if left == None and right == None:
                return True

            if left == None or right == None:
                return False

            return (left.val == right.val) and (isMirror(left.left, right.right) and isMirror(left.right, right.left))
        
        return isMirror(root.left, root.right)
        
        
        # apprach 2. Iteration using deque
        from collections import deque
        
        if root == None:
            return True
        
        q = deque([])
        q.append(root.left)
        q.append(root.right)

        while len(q) != 0:
            left = q.popleft()
            right = q.popleft()

            if left == None and right == None:
                continue

            if left == None or right == None:
                return False

            if left.val != right.val:
                return False

            q.append(left.left)
            q.append(right.right)
            q.append(left.right)
            q.append(right.left)

        return True
    
        # approach 3. Iteration using stack
        if root == None:
            return True
        
        stack = []
        stack.append(root.left)
        stack.append(root.right)
        
        while len(stack) != 0:
            node1 = stack.pop()
            node2 = stack.pop()
            
            if node1 == None and node2 == None:
                continue
            
            if node1 == None or node2 == None:
                return False
            
            if node1.val != node2.val:
                return False
            
            stack.append(node1.left)
            stack.append(node2.right)
            stack.append(node1.right)
            stack.append(node2.left)
        
        return True
        