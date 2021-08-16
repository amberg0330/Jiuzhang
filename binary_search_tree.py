
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None

#BST 插入
class BST:
    def __init__(self):
        self.__root = None #__root 私有变量

    def add(self, val):
        self.__root = self.__add_helper(self.__root, val)

    def __add_helper(self, root, val): #私有变量
        if not root:
            return TreeNode(val)
        if root.val > val:
            root.left = self.__add_helper(root.left, val)
        else:
            root.right = self.__add_helper(root.right, val)
        return root

#BST 查找
    def contains(self, val):
        return self.__contains_helper(self.__root, val)

    def __contains_helper(self, root, val):
        if not root:
            return False
        if root.val == val:
            return True
        elif root.val > val:
            return self.__contains_helper(root.left, val)
        else:
            return self.__contains_helper(root.right, val)

