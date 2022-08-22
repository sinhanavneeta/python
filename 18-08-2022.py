"""
Problem 1:
Given a positive number, return the square root of it. If the number is not a perfect
square, return the floor of its square root.

"""
import math


def calSquareRoot(n) :
    return math.floor(math.sqrt(n))
print(calSquareRoot(5))
print(calSquareRoot(11))
print(calSquareRoot(9))

"""
Problem 2:
Given the root of a binary tree, invert the tree, and return its root.
Input:
=====
 (4) 
/ \
(7) (2) 
/ \ / \
(9) (6) (3) (1) 
output:
======
 (4)
 / \
 (2) (7)
 / \ / \
(1) (3) (6) (9)

"""
class BinaryTreeNode:
    def __init__(self, value):
        self.value = value
        self.leftChild = None
        self.rightChild = None

root = BinaryTreeNode(4)
node1 = BinaryTreeNode(7)
node2 = BinaryTreeNode(2)
node3 = BinaryTreeNode(9)
node4 = BinaryTreeNode(6)
node5 = BinaryTreeNode(3)
node6 = BinaryTreeNode(1)

root.leftChild = node1
root.rightChild = node2
node1.leftChild = node3
node1.rightChild = node4
node2.leftChild = node5
node2.rightChild = node6


print("Before Swapping: ")
print(root.value, end=" ")
print(node1.value, end=" ")
print(node2.value, end=" ")
print(node3.value, end=" ")
print(node4.value, end=" ")
print(node5.value, end=" ")
print(node6.value)


temp = BinaryTreeNode(0)

temp.value = node1.leftChild.value
node1.leftChild.value = node2.rightChild.value
node2.rightChild.value = temp

temp.value = node1.rightChild.value
node1.rightChild.value = node2.leftChild.value
node2.leftChild.value = temp

temp.value = root.leftChild.value
root.leftChild.value = root.rightChild.value
root.rightChild.value = temp.value

print("After Swapping: ")
print(root.value, end=" ")
print(node1.value, end=" ")
print(node2.value, end=" ")
print(node3.value, end=" ")
print(node4.value, end=" ")
print(node5.value, end=" ")
print(node6.value)
"""
# def swapNodesUtil(root, level, k):
#     if root is None or (root.leftChild is None and root.rightChild):
#
# def swapNodes(root, k):
#     swapNodesUtil(root, 1, k)
"""


