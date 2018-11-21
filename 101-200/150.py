class Solution:
    def evalRPN(self, tokens):
        """
        :type tokens: List[str]
        :rtype: int
        """
        def calculate(n1,n2,operator):
            #n1=int(n1);n2=int(n2)
            if operator=='+':
                return n1+n2
            if operator=='-':
                return n1-n2
            if operator=='*':
                return n1*n2
            if operator=='/':
                res=abs(n1)//abs(n2)
                if n1*n2<0:
                    return -1*res
                else:
                    return res
        stack=[]
        ops={'+','-','*','/'}
        for t in tokens:
            if t not in ops:
                stack.append(int(t))
            else:
                n2=stack.pop()
                n1=stack.pop()
                cal=calculate(n1,n2,t)
                stack.append(cal)
        return int(stack[0])
