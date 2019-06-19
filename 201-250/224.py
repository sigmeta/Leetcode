class Solution:
    def calculate(self, s: str) -> int:
        res=0;sign=1;n=0;stack=[]
        for c in s:
            if c==' ':
                continue
            elif c>='0' and c<='9':
                n=n*10+int(c)
            elif c=='+':
                res+=n*sign
                sign=1
                n=0
            elif c=='-':
                res+=n*sign
                sign=-1
                n=0
            elif c=='(':
                stack.append([res,sign])
                res=0;n=0;sign=1
            elif c==')':
                res+=n*sign
                n=res
                res,sign=stack.pop()
        res+=n*sign
        return res
