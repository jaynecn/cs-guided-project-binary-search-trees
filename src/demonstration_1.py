"""
You are given a binary tree.

Write a function that can find the **maximum depth** of the binary tree. The
maximum depth can be defined as the number of nodes found along the longest
path from the root down to the furthest leaf node. Remember, a leaf node is a
node that has no children.

Example:

Given the following binary tree

    5
   / \
  12  32
     /  \
    8    4

your function should return the depth = 3.
"""
class BinaryTreeNode:
    def __init__(self, value=0, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

def insert(self, value):
    # new node
    new_node = BinaryTreeNode(value)
    
    if value < self.value:
      # insert to the left
      if self.left is None:
        self.left = new_node
      else:
        self.left.insert(value)
      
    else:
      # insert to the right
      if self.right is None:
        self.right = new_node
      else:
        self.right.insert(value)

def maxDepth(self, root):
    
    # solve case with no children
    if self.left is None and self.right is None:
        return 1
    left_height = 0
    right_height = 0
    
    if self.left is not None:
        left_height = self.left.maxDepth()
        return left_height
        
    if self.right is not None:
        right_height = self.right.maxDepth()
        return right_height
    
    max_depth = max(left_height, right_height)
    return max_depth + 1

root = BinaryTreeNode(8)

        

