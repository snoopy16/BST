# BST
Repo to perform basic CRUD operations on Binary Search Trees

## What is a Binary Search Tree ?
A tree is nonlinear data structure compared to arrays, linked lists, stacks and queues which are linear data structures.
A tree can be empty with no nodes or a tree can have just one node called root and zero or more subtrees

## Terminology
Before learning to work with BSTs, lets first understand the basic terminilogy - 

* Leaves: Nodes with no children or external nodes
* internal nodes: Nodes which are not leaves. Internal nodes have at least one child
* Siblings: Nodes with the same parent are called siblings
* Depth of a node: number of edges from root to the node
* Height of a node: number of edges from node to the deepest leaf
* height of tree: height of a root

## Basic Tree Operations
There are many basic operations you can perform on a BST. When implementing these in code, you've to use recursion to get the part of the tree where you need to operate. In general there are 4 basic operations for BST - 

### Traversal
Depth First Search (DFS): the search tree is deepened as much as possible before going
                          to the next sibling
<screenshot>
Indorder: LNR (ABCDEFGHI)
Preorder: NLR (FBADCEGIH)
Postorder: LRN (ACEDBHIGF)

### Node Addition

Adding a node to a tree requires traversing the part of the tree where the node belongs. For example, if the node to add is less than the root node then you should traverse the `left sub-tree` to find a suitable position to add the node. You cannot add duplicate nodes to a tree.

### Node Search

When searching for a node, you've to determine which side of the tree you should search depending on the value of the root node. If the root node is greater than the node to be searched, look for node in the right sub-tree else look for node in the left sub-tree. 

### Node Deletion

This one is more involved than just tranversing and deleting nodes. In addition to traversing the tree, you also need to re-adjust the tree depending on how many children it has. Generally speaking, there are 3 cases -

1. when the element to delete is a leaf
2. when the element to delete has one child (left child or right child)
3. when the element to delete has 2 children

Different strategies are used for each. When you look at the code, those will be outlined clearly.
