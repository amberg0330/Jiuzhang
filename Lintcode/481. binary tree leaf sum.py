# Description
# Given a binary tree, calculate the sum of leaves.
#
# Example
# Example 1:
#
# Input：{1,2,3,4}
# Output：7
# Explanation：
#     1
#    / \
#   2   3
#  /
# 4
# 3+4=7
# Example 2:
#
# Input：{1,#,3}
# Output：3
# Explanation：
#     1
#       \
#        3
#
class Solution:
    def leafSum(self, root):
        self.res = 0
        self.helper(root)
        return self.res

    def helper(self, root):
        if not root:
            return
        else:
            if not root.left and not root.right:
                self.res += root.val
            self.helper(root.right)
            self.helper(root.left)
