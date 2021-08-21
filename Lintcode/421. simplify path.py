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