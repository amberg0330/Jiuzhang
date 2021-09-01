# Description
# Find the Nth number in Fibonacci sequence.
#
# A Fibonacci sequence is defined as follow:
#
# The first two numbers are 0 and 1.
# The i th number is the sum of i-1 th number and i-2 th number.
# The first ten numbers in Fibonacci sequence is:
#
# 0, 1, 1, 2, 3, 5, 8, 13, 21, 34 ...
#
# N <= 20

# method 1: iteration
class Solution:
    """
    @param n: an integer
    @return: an ineger f(n)
    """
    def fibonacci(self, n):
        if n < 1:
            return -1
        if n == 1:
            return 0

        first, second = 0, 1
        cnt = 2

        while cnt < n:
            third = first + second
            first, second = second, third
            cnt += 1

        return second

# method 2: recursion -- 这个方法有许多duplicate calculation
class Solution:
    """
    @param n: an integer
    @return: an ineger f(n)
    """
    # 递归三要素之一： 递归定义
    def fibonacci(self, n):
        # 特殊情况处理
        if n < 1:
            return -1
        # 递归三要素之三： 递归出口
        if n == 1:
            return 0
        if n == 2:
            return 1
        # 递归三要素之二：递归拆解
        return self.fibonacci(n - 1) + self.fibonacci(n - 2)

# method 3: recursion + 记忆化搜索
# 有点像动态规划
class Solution:
    """
    @param n: an integer
    @return: an ineger f(n)
    """
    def fibonacci(self, n):
        if n < 1:
            return -1
        if n == 1:
            return 0
        arr = [0 for _ in range(n + 1)]
        arr[2] = 1
        return self.get_fibonacci(n, arr)

    def get_fibonacci(self, n, arr):
        if n == 1 or n == 2 or arr[n]>0:
            return arr[n]
        arr[n] = self.get_fibonacci(n - 1, arr) + self.get_fibonacci(n - 2, arr)
        return arr[n]
