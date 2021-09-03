# Description
# Consider all the leaves of a binary tree.  From left to right order, the values of those leaves
# form a leaf value sequence.
#
# For example, in the given tree above, the leaf value sequence is (6, 7, 4, 9, 8).
#
# Two binary trees are considered leaf-similar if their leaf value sequence is the same.
#
# Return true if and only if the two given trees with head nodes root1 and root2 are leaf-similar.
# Otherwise, return false.
#
# Both of the given trees will have between 1 and 100 nodes.
#
# Example
# Example 1:
#
# Input: {1,#,2,3}, {1,2,#,3}
# Output:
# Explaination:
# the first tree:
#   1
#     \
#      2
#     /
#    3
# the second tree:
#     1
#    /
#   2
#  /
# 3
# The leaf value sequence is: [3], so the same
# Example 2:
#
# Input: {1,#,2,3}, {1,2,#,3}
# Output:
# Explaination:
# the first tree:
#   1
#     \
#      2
#     /
#    3
# the second tree:
#    1
#   / \
#  2   3
# The first leaf value sequence is: [3], the second tree is: [2, 3], so it is not the same

"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""

class Solution:
    """
    @param root1: the first tree
    @param root2: the second tree
    @return: returns whether the leaf sequence is the same
    """

    def leafSimilar(self, root1, root2):
        list1 = []
        list2 = []
        if not root1 and not root2:
            return True
        elif not root1 or not root2:
            return False
        else:
            def dfs(node, mylist):
                if not node.left and not node.right:
                    mylist.append(node.val)
                if node.left:
                    dfs(node.left, mylist)
                if node.right:
                    dfs(node.right, mylist)
                return mylist

            list1 = dfs(root1, list1)
            list2 = dfs(root2, list2)

            return list1 == list2


