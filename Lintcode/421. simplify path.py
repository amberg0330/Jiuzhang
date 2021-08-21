# Description
# Given an absolute path for a file (Unix-style), simplify it.

# In a UNIX-style file system, a period . refers to the current directory. Furthermore, a double period .. moves the directory up a level.

# The result must always begin with /, and there must be only a single / between two directory names. The last directory name (if it exists) must not end with a trailing /. Also, the result must be the shortest string representing the absolute path.

# Did you consider the case where path is "/../"?

# In this case, you should return "/".

# Another corner case is the path might contain multiple slashes '/' together, such as "/home//foo/".

# In this case, you should ignore redundant slashes and return "/home/foo".

# Example 2:

# Input: "/a/./../../c/"
# Output: "/c"
# Explanation: "/" has no parent directory, so "/../" equals "/".



class Solution: 

    def simplifyPath(self, path):
        arr = path.split('/')
        mystack = [] # 用list实现stack
        for s in arr: 
            if s == "..": 
                if mystack: 
                    mystack.pop()
            elif s == '' or s == '.': 
                continue 
            else: 
                mystack.append(s)
        if not mystack: 
            return '/'

        mystring = ''

        while mystack: 
            mystring += '/' + mystack.pop()
        
        return mystring 