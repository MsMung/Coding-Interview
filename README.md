# Coding-Interview

## Trees

### Tree

A linked data structure consisting of a root node, and each of its node can have multiple pointers to child nodes.

### Binary tree

A tree where the maximum number of child nodes is 2.

### Binary search tree

A binary tree where for each node, every value in its left subtree is `less than (or equal to)` the value in the node itself, and every value in its right subtree is `greater than (or equal to)` the value in the node itself.

In order traversal of a BST will give you all elements in order.

### Tree traversals

Visiting each node in a tree `exactly once`.

#### Breadth first

Visit nodes in order of their `distance` from the root.

#### Depth first

Traverse each path, going as `deep` as possible while visiting unvisited nodes.

#### Pre order

Same as depth first.

For each node, visit it, them traverse each of ites subtrees (root -> left -> right).

#### Post order

For each node, tracerse each of its subtrees, then visit the node itself (left -> right -> root).

#### In order

For binary (search) trees only.

For each node, traverse its left subtree, then visit the node itself, then traverse its right subtree.
