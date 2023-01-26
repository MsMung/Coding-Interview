class BinaryTreeNode:
    """
    A node in a binary tree.
    """
    def __init__(self, data, left=None, right=None):
        """ (BinaryTreeNode, str, BinaryTreeNode, BinaryTreeNode) -> NoneType

        Initialize a new BinaryTreeNde with data, left and right children.
        """
        self._data = data
        self._left = left
        self._right = right

    def __repr__(self):
        """ (BinaryTreeNode) -> str
        
        Return a string representing <self>.
        """ 
        return ("BinaryTreeNode(" + repr(self._data) + ", " +
        repr(self._left) + ", " + repr(self._right) + ")")

    def get_data(self):
        """ (BinaryTreeNode) -> str
        """
        return self._data

    def set_data(self, data):
        """ (BinaryTreeNode, str) -> NoneType
        """
        self._data = data

    def get_left(self):
        """ (BinaryTreeNode) -> BinaryTreeNode
        """
        return self._left

    def set_left(self, left):
        """ (BinaryTreeNode, BinaryTreeNode) -> NoneType
        """
        self._left = left

    def get_right(self):
        return self._right

    def set_right(self, right):
        self._right = right

def bst_search(root, value):
    """ (BinaryTreeNode, str) -> bool
    
    Return True iff the BST rooted at <root>
    contains a node whose data is <value>.
    """
    curr = root
    while (curr != None and curr.get_data() != value):
        if value < curr.get_data():
            curr = curr.get_left()
        else:
            curr = curr.get_right()
    
    return (curr != None)

def bst_insert(root, value):
    """(BinaryTreeNode, str) -> BinaryTreeNode

    Insert a (possibly duplicate) node whose data is <value>
    into the BST rooted at <root>.
    Return the root of the updated BST.
    """
    new_node = BinaryTreeNode(value)
    
    if root == None:
        root = new_node
        return root

    parent = None
    curr = root
    while (curr != None):
        parent = curr
        if value < curr.get_data():
            curr = curr.get_left()
        else:
            curr = curr.get_right()

    if value < parent.get_data():
        parent.set_left(new_node)
    else:
        parent.set_right(new_node)
    
    return root

