# This is file to perform basic operations on BST
# Author: Nidhi Tare
# Operations: Create BST, Insert node, Delete Node, Traverse a Tree (Inorder, PreOrder, PostOrder), Search node

# Define a basic tree/node
class Node:
    # Attributes: node value, left child, right child
    # define constructor to initialize a tree
    def __init__(self, key):
        self.val = key
        self.left = None
        self.right = None

def insertNode(node, key):
    # Insert a node in a tree
    if node is None: # Empty tree, add the node
        return Node(key)

    if key < node.val:
        # Add node to the left subtree
        node.left = insertNode(node.left, key)
    elif key > node.val:
        # Add the node to the right subtree
        node.right = insertNode(node.right, key)
    else:
        # Adding a duplicate node to a tree
        print("Can't add duplicate node to the tree")

    # Return the unchanged node pointer
    return node


def printInorder(root):
    # Prints the BST in Inorder: LNR
    if root:
        # Print left sub-tree
        printInorder(root.left)

        # Print the node
        print(root.val, end=' ')

        # Print the right sub-tree
        printInorder(root.right)

def printPostOrder(root):
    # Prints the BST in PostOrder: LRN
    if root:
        # Print left sub-tree
        printInorder(root.left)

        # Print the right sub-tree
        printInorder(root.right)

        # Print the node
        print(root.val, end=' ')


def printPreOrder(root):
    # Prints the BST in PreOrder: NLR
    if root:
        # Print the node
        print(root.val, end=' ')

        # Print left sub-tree
        printInorder(root.left)

        # Print the right sub-tree
        printInorder(root.right)



def searchNode(root, value):
    # Search a node in a tree with value "value"
    # if found, return the node or None

    if root is None or root.val == value: # if it is an empty tree return the root or if key is present at root
        return root

    if value < root.val:
        # the node is in the left sub-tree
        return searchNode(root.left, value)
    else:        # the node is in the right sub-tree
        return searchNode(root.right, value)

def binary_search_tree():
    # Main method where we will be doing CRUD operations on BST
    # Populate a tree
    #node = Node(8) # root of the tree
    node = insertNode(None, 3)  # 3 will be added as a left child to the tree (3 < 8)
    insertNode(node, 8)
    insertNode(node, 11)
    insertNode(node, 10)
    insertNode(node, 0)
    insertNode(node, 2)
    insertNode(node, 4)
    insertNode(node, 5)

    #print(node.val, node.right, node.left)
    # traverse the tree - Inorder/PreOrder/PostOrder
    print("\nInOrder: ")
    printInorder(node)
    print("\nPostOrder: ")
    printPostOrder(node)
    print("\nPreOrder: ")
    printPreOrder(node)
    print("\n")

    # Search a node in BST
    key = 5
    s = searchNode(node, key)
    if s is None:
        print(key, "not found")
    else:
        print(key, "found")

    # Delete a node

if __name__ == '__main__':
    binary_search_tree()

