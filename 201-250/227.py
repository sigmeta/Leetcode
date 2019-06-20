class Solution:
    def calculate(self, s: str) -> int:
        stack=[];res=0;n=0;prior={'+':0,'-':0,'*':1,'/':1};op='+'
        def cal(a,b,op):
            if op=='+':
                return a+b
            elif op=='-':
                return a-b
            elif op=='*':
                return a*b
            elif op=='/':
                return a//b
            
        for c in s:
            if c==' ':
                continue
            elif c>='0' and c<='9':
                n=n*10+int(c)
            elif c in prior:
                if prior[c]>prior[op]:
                    stack.append([res,op])
                    res=n
                    op=c
                elif prior[c]==prior[op]:
                    res=cal(res,n,op)
                    op=c
                elif prior[c]<prior[op]:
                    res=cal(res,n,op)
                    if stack:
                        n=res
                        res,op=stack.pop()
                        res=cal(res,n,op)
                        op=c
                n=0
        res=cal(res,n,op)
        if stack:
            n=res
            res,op=stack.pop()
            res=cal(res,n,op)
        return res
