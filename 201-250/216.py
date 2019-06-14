class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        candidates=[1,2,3,4,5,6,7,8,9]
        self.res=[]
        self.dfs(candidates,k,n,[])
        return self.res
    def dfs(self,can,k,n,nlist):
        if k==0 and n==0:
            self.res.append(nlist)
            return
        elif not can:
            return
        for i in range(len(can)):
            self.dfs(can[i+1:],k-1,n-can[i],nlist+[can[i]])
