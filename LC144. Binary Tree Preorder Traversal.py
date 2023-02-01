# 144. Binary Tree Preorder Traversal
# https://leetcode.com/problems/binary-tree-preorder-traversal/description/

'''
Given the root of a binary tree, 
return the preorder traversal of its nodes' values.
'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    # time complexity: O(n), visit each node once and 
    # perform a constant amount of work at each node
    # space complexity: O(n), recursive call stack
    # the call stack takes up space equivalent to the depth of the tree,
    # worst case when the tree is skewed -> O(n)
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        result = []

        def dfs(root):
            # start with root node, if root is not None
            # add root's value to result, 
            # repeat the step with root's left child
            # repeat the step with root's right child
            # if root == None:
            #     return
            if root != None:
                result.append(root.val)
                dfs(root.left)
                dfs(root.right)
            # the return below is optional since
            # If the function doesn't have any return statement,
            # then it returns None
            #return

        dfs(root)
        return result

# to visualize above code: https://pythontutor.com/visualize.html#code=class%20TreeNode%3A%0A%20%20%20%20def%20__init__%28self,%20val%3D0,%20left%3DNone,%20right%3DNone%29%3A%0A%20%20%20%20%20%20%20%20self.val%20%3D%20val%0A%20%20%20%20%20%20%20%20self.left%20%3D%20left%0A%20%20%20%20%20%20%20%20self.right%20%3D%20right%0A%0Aclass%20Solution%3A%0A%20%20%20%20def%20preorderTraversal%28self,%20root%29%3A%0A%20%20%20%20%20%20%20%20result%20%3D%20%5B%5D%0A%0A%20%20%20%20%20%20%20%20def%20dfs%28root%29%3A%0A%20%20%20%20%20%20%20%20%20%20%20%20%23%20start%20with%20root%20node,%20if%20root%20is%20not%20None%0A%20%20%20%20%20%20%20%20%20%20%20%20%23%20add%20root's%20value%20to%20result,%20%0A%20%20%20%20%20%20%20%20%20%20%20%20%23%20repeat%20the%20step%20with%20root's%20left%20child%0A%20%20%20%20%20%20%20%20%20%20%20%20%23%20repeat%20the%20step%20with%20root's%20right%20child%0A%20%20%20%20%20%20%20%20%20%20%20%20if%20root%20%3D%3D%20None%3A%0A%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20return%0A%20%20%20%20%20%20%20%20%20%20%20%20result.append%28root.val%29%0A%20%20%20%20%20%20%20%20%20%20%20%20dfs%28root.left%29%0A%20%20%20%20%20%20%20%20%20%20%20%20dfs%28root.right%29%0A%0A%20%20%20%20%20%20%20%20dfs%28root%29%0A%20%20%20%20%20%20%20%20return%20result%0A%20%20%20%20%20%20%20%20%0Asolution%20%3D%20Solution%28%29%0Aroot%20%3D%20TreeNode%281%29%0Aroot_right%20%3D%20TreeNode%282%29%0Aroot.right%20%3D%20root_right%0Aroot_right.left%20%3D%20TreeNode%283%29%0Asolution.preorderTraversal%28root%29&cumulative=false&curInstr=63&heapPrimitives=nevernest&mode=display&origin=opt-frontend.js&py=3&rawInputLstJSON=%5B%5D&textReferences=false

        # Approach 2. Iteration
        '''
        can implement DFS iteratively using a stack 
        since stack is last in first out,
        we need to add the right child before the left child
        to access the left child before the right child
        '''
        # version 1
        result = []
        stack = [root]

        while len(stack) != 0:
            top_node = stack.pop()
            if top_node != None:
                result.append(top_node.val)
                stack.append(top_node.right)
                stack.append(top_node.left)

        return result
    
        # version 2
        result = []
        stack = []
        curr = root

        while stack or curr != None:
            if curr != None:
                result.append(curr)
                # add before going to children
                result.append(curr.val)
                curr = curr.left
            else:
                node = stack.pop()
                curr = node.right

        return result
        
        