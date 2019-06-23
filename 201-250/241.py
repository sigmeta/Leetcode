class Solution:
    def diffWaysToCompute(self, input: str) -> List[int]:
        if not input:
            return []
        if input.isdigit():
            return [int(input)]
        res=[]
        for i in range(len(input)):
            if not (input[i]=='+' or input[i]=='-' or input[i]=='*'):
                continue
            left=self.diffWaysToCompute(input[:i])
            right=self.diffWaysToCompute(input[i+1:])
            for l in left:
                for r in right:
                    if input[i]=='+':
                        res.append(l+r)
                    elif input[i]=='-':
                        res.append(l-r)
                    elif input[i]=='*':
                        res.append(l*r)
        return res
        
