# Description
# Follow up Zigzag Iterator: What if you are given k 1d vectors? How well can your code be extended to such cases? The "Zigzag" order
# is not clearly defined and is ambiguous for k > 2 cases. If "Zigzag" does not look right to you, replace "Zigzag" with "Cyclic".

# Example
# Example1

# Input: k = 3
# vecs = [
#     [1,2,3],
#     [4,5,6,7],
#     [8,9],
# ]
# Output: [1,4,8,2,5,9,3,6,7]
# Example2

# Input: k = 3
# vecs = [
#     [1,1,1]
#     [2,2,2]
#     [3,3,3]
# ]
# Output: [1,2,3,1,2,3,1,2,3]
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

## Method 2. 用Deque的自带属性
class ZigzagIterator2:
    """
    @param: vecs: a list of 1d vectors
    """

    def __init__(self, vecs):
        # do intialization if necessary
        self.queue = collections.deque()
        for vec in vecs:
            if len(vec) > 0:
                self.queue.append([iter(vec), len(vec)])

    """
    @return: An integer
    """

    def _next(self):
        vec_iter, vec_len = self.queue.popleft()
        value = next(vec_iter)
        vec_len -= 1
        if vec_len > 0:
            self.queue.append([vec_iter, vec_len])
        return value

    """
    @return: True if has next
    """

    def hasNext(self):
        return len(self.queue) > 0
