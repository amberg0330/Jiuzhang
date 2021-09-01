# Description
# Given a binary tree, return the zigzag level order traversal of its nodes' values.
# (ie, from left to right, then right to left for the next level and alternate between).
#
# Example
# Example 1:
#
# Input:
#
# tree = {1,2,3}
# Output:
#
# [[1],[3,2]]
# Explanation:
#
#     1
#    / \
#   2   3
# it will be serialized {1,2,3}
# Example 2:
#
# Input:
#
# tree = {3,9,20,#,#,15,7}
# Output:
#
# [[3],[20,9],[15,7]]
# Explanation:
#
#     3
#    / \
#   9  20
#     /  \
#    15   7
# it will be serialized {3,9,20,#,#,15,7}
"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""

# method1：用 queue来做
import collections

class Solution:
    """
    @param root: A Tree
    @return: A list of lists of integer include the zigzag level order traversal of its nodes' values.
    """
    def zigzagLevelOrder(self, root):
        mylist = []
        if not root:
            return mylist
        #BFS 用到队列
        q = collections.deque()
        is_left_to_right = True
        q.append(root)

        while len(q) != 0:
            # 逐层遍历：记录当前queue的size，然后遍历size个元素
            size = len(q)
            # 存放当前层元素的list
            l = []
            for i in range(size):
                # 从queue中取一个点
                node = q.popleft()
                # 加入当前层的list
                l.append(node.val)
                # 如果右孩子不为空，入队
                # Q: 是否可以不在这里查null，直接入队呢？
                # A: 可以，但是需要： 1. 加一个logic：如果null，continue 2. 如果list最好为空不要计入list
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            if not is_left_to_right:
                l.reverse()
            mylist.append(l)
            is_left_to_right = not is_left_to_right
        return mylist

# method 2: BFS + stack
class Solution:
    def zigzagLevelOrder(self, root):
        mylist = []
        if not root:
            return list
        # 初始化两个stack 交替存放下一层nodes
        stack1 = []
        stack2 = []
        stack1.append(root)
        left_to_right = True

        while len(stack1) != 0:
            # 存放当前层的node
            l = []
            # stack中装了一层node, 取出当前stack所有的node
            while len(stack1) != 0:
                # 弹出当前node
                curr_node = stack1.pop()
                # 如果node为None continue
                if not curr_node:
                    continue
                # 当前node进入当前层list
                l.append(curr_node.val)
                # 如果当前层从左向右，先加左孩子，后加右孩子
                if left_to_right:
                    stack2.append(curr_node.left)
                    stack2.append(curr_node.right)
                # 如果当前层从右向左，先加右孩子 后加左孩子
                else:
                    stack2.append(curr_node.right)
                    stack2.append(curr_node.left)
            # 反转方向
            left_to_right = not left_to_right
            # 注意：list中有东西的时候，才加入mylist
            # mylist有可能空，因为当前层都是None
            if len(l) > 0:
                mylist.append(l)

            stack1, stack2 = stack2, stack1
        return mylist

