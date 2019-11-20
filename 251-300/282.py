class Solution:
    def addOperators(self, num: str, target: int) -> List[str]:
        def cal(num,target,plist,pn,ans):
            if target==ans and len(num)==0:
                self.result.append(plist)
                return 0
            for i in range(1,len(num)+1):
                if num[0]=='0' and i>1:
                    break
                a=int(num[:i])
                if plist=='':
                    cal(num[i:],target,num[:i],a,a)
                else:
                    cal(num[i:],target,plist+'+'+num[:i],a,ans+a)
                    cal(num[i:],target,plist+'-'+num[:i],-a,ans-a)
                    cal(num[i:],target,plist+'*'+num[:i],pn*a,ans+pn*a-pn)
        self.result=[]
        cal(num,target,'',0,0)
        return self.result
