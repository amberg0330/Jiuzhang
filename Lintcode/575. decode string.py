# Description
# Given an expression s contains numbers, letters and brackets. Number represents the number of repetitions inside the brackets(can be a string or another expression)．Please expand expression to be a string.

# Numbers can only appear in front of “[]”.

# Example
# Example1

# Input: S = abc3[a]
# Output: "abcaaa"
# Example2

# Input: S = 3[2[ad]3[pf]]xyz
# Output: "adadpfpfpfadadpfpfpfadadpfpfpfxyz"

class Solution:
    """
    @param s: an expression includes numbers, letters and brackets
    @return: a string
    """
    def expressionExpand(self, s):
        mystack = []
        num = 0 
        for ch in s: 
            if ch.isdigit():
                num = num * 10 + int(ch)
            # 如果是"[", 把数字压线
            elif ch == "[":
                mystack.append(num)
                num = 0 #reset 数字！
            # 如果是"]", 把string弹出 练成一个string
            # 然后把数字弹出 
            elif ch == "]":
                strs = []
                while mystack and not isinstance(mystack[-1], int):
                    strs.append(mystack.pop())
                strs.reverse()
                repeat_s = mystack.pop()
                for _ in range(repeat_s): 
                    mystack.append("".join(strs))
            # 如果是字母 直接压栈
            else:
                mystack.append(ch)
            
        
        strs = []
        while mystack:
            strs.append(mystack.pop())
        # 翻转 list
        strs.reverse()
        # 链接 list
        return ''.join(strs)






