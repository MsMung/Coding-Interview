# 701. Insert into a Binary Search Tree
# https://leetcode.com/problems/insert-into-a-binary-search-tree/description/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        new_node = TreeNode(val)
        if root == None:
            root = new_node
            return root

        parent = None
        curr = root
        while (curr != None):
            parent = curr
            if val < curr.val:
                curr = curr.left
            else:
                curr = curr.right
        
        if val < parent.val:
            parent.left = new_node
        else:
            parent.right = new_node
        
        return root

# Leetcode solution
'''
The problem solution: one could always
insert new code as a child of the leaf.
'''
# Approach 1. Recursion
# time complexity: O(H) where H is the tree height.
# that results in O(logN) in the average case, O(N) in the worst case

# space complexity: O(H) to keep the recursion stack
# O(logN) in the average case, and O(N) in the worst case
class Solution:
    def insertIntoBST(self, root: TreeNode, val: int) -> TreeNode:
        if not root:
            return TreeNode(val)
        
        if val > root.val:
            # insert into the right subtree
            root.right = self.insertIntoBST(root.right, val)
        else:
            root.left = self.insertIntoBST(root.left, val)
        return root

# to visualize the recursion: https://pythontutor.com/visualize.html#mode=display
# run with code below:
'''
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def insertIntoBST(self, root: TreeNode, val: int) -> TreeNode:
        if not root:
            return TreeNode(val)
        
        if val > root.val:
            # insert into the right subtree
            root.right = self.insertIntoBST(root.right, val)
        else:
            # insert into the left subtree
            root.left = self.insertIntoBST(root.left, val)
        return root
    
    
root = TreeNode(4)
root.left = TreeNode(2)
root.left.left = TreeNode(1)
root.left.right = TreeNode(3)
root.right = TreeNode(7)

val = 5
solution = Solution()
print(solution.insertIntoBST(root, val))
'''

# Approach 2. Interation
# time complexity O(H), space complexity O(1)
class Solution:
    def insertIntoBST(self, root, val):
        node = root
        while node:
            # insert into the right subtree
            if val > node.right:
                # insert right now
                if not node.right:
                    node.right = TreeNode(val)
                    return root
                else:
                    node = node.right
            
            else:
                if not node.left:
                    node.left = TreeNode(val)
                    return root
                else:
                    node = node.left
        return TreeNode(val) # if empty tree
