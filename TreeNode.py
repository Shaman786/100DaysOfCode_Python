""" Python3 code for inorder successor
and predecessor of tree """

# A Binary Tree Node
# Utility function to create a new tree node


class newNode:

    # Constructor to create a new node
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

# function to find left most node in a tree


def leftMostNode(node):

    while (node != None and node.left != None):
        node = node.left
    return node

# function to find right most node in a tree


def rightMostNode(node):
    while (node != None and node.right != None):
        node = node.right
    return node

# recursive function to find the Inorder Successor
# when the right child of node x is None


def findInorderRecursive(root, x):

    if (not root):
        return None
    if (root == x or (findInorderRecursive(root.left, x)) or
            (findInorderRecursive(root.right, x))):
        if findInorderRecursive(root.right, x):
            temp = findInorderRecursive(root.right, x)
        else:
            temp = findInorderRecursive(root.left, x)
        if (temp):

            if (root.left == temp):

                print("Inorder Successor of",
                      x.data, end="")
                print(" is", root.data)
                return None
        return root
    return None

# function to find inorder successor
# of a node


def inorderSuccessor(root, x):

    # Case1: If right child is not None
    if (x.right != None):
        inorderSucc = leftMostNode(x.right)
        print("Inorder Successor of", x.data,
              "is", end=" ")
        print(inorderSucc.data)

    # Case2: If right child is None
    if (x.right == None):
        f = 0
        rightMost = rightMostNode(root)

        # case3: If x is the right most node
        if (rightMost == x):
            print("No inorder successor!",
                  "Right most node.")
        else:
            findInorderRecursive(root, x)


# Driver Code
if __name__ == '__main__':

    root = newNode(1)
    root.left = newNode(2)
    root.right = newNode(3)
    root.left.left = newNode(4)
    root.left.right = newNode(5)
    root.right.right = newNode(6)

    # Case 1
    inorderSuccessor(root, root.right)

    # case 2
    inorderSuccessor(root, root.left.left)

    # case 3
    inorderSuccessor(root, root.right.right)

# This code is contributed
# by SHUBHAMSINGH10
