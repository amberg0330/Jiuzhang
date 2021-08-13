# Method 1. 双指针解法
class ZigzagIterator2:
    """
    @param: vecs: a list of 1d vectors
    """

    def __init__(self, vecs):
        # do intialization if necessary
        self.row_ind = 0
        self.col_ind = 0
        self.vecs = vecs
        # 非空行计数器
        self.non_empty_vec_cnt = len(self.vecs)
        for i in range(len(self.vecs)):
            if len(self.vecs[i]) == 0:
                self.non_empty_vec_cnt -= 1

    """
    @return: An integer
    """

    def _next(self):
        mylist = []
        while self.hasNext():
            # 跳过所有已终结的行 找到下一个可以返回的行:
            while self.col_ind >= len(self.vecs[self.row_ind]):
                self.row_ind += 1
                if self.row_ind == len(self.vecs):
                    self.row_ind = 0
                    self.col_ind += 1
            value = self.vecs[self.row_ind][self.col_ind]
            if self.col_ind == len(self.vecs[self.row_ind]) - 1:
                self.non_empty_vec_cnt -= 1
            # 行 +1
            self.row_ind += 1
            if self.row_ind == len(self.vecs):
                self.row_ind = 0
                self.col_ind += 1

            return value

    """
    @return: True if has next
    """

    def hasNext(self):
        # write your code here
        # 如果所有行都被用掉 返回false
        return self.non_empty_vec_cnt > 0


# Your ZigzagIterator2 object will be instantiated and called as such:
# solution, result = ZigzagIterator2(vecs), []
# while solution.hasNext(): result.append(solution.next())
# Output result