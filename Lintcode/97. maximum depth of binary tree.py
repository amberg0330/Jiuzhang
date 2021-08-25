# Description
# Given a binary tree, find its maximum depth.
# The maximum depth is the number of nodes along the longest path from the root node down to
# the farthest leaf node.
# The answer will not exceed 5000
#
# Example
#
# Example 1:
# Input:
# tree = {}
# Output:
# 0
# Explanation:
# The height of empty tree is 0.
#
# Example 2:
# Input:
# tree = {1,2,3,#,#,4,5}
# Output:
# 3
# Explanation:
# Like this:
# 1
# / \
# 2   3
# /  \
# 4    5
# it will be serialized {1,2,3,#,#,4,5}

"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""

class Solution:
    """
    @param root: The root of binary tree.
    @return: An integer
    """
    def maxDepth(self, root):
        self.res = 0
        self.helper(root, 1)
        return self.res

    def helper(self, root, height):
        if not root:
            return
        else:
            self.res = max(height, self.res)
            self.helper(root.left, height + 1)
            self.helper(root.rigt, height + 1)


