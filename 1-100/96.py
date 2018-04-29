class Solution0:  #递归的方法超时
    def numTrees(self, n):
        """
        :type n: int
        :rtype: int
        """ 
        return self.dfs(1,n+1)
    def dfs(self,s,e):
        if s==e or s==e-1:
            return 1
        res=0
        for i in range(s,e):
            res+=self.dfs(s,i)*self.dfs(i+1,e)
        return res
        
class Solution:#动态规划方法通过，dp[n]存的是n时搜索树的数量
    def numTrees(self, n):
        """
        :type n: int
        :rtype: int
        """ 
        dp=[0 for i in range(n+1)]
        dp[0]=1
        for i in range(1,n+1):
            for j in range(i):
                dp[i]+=dp[j]*dp[i-1-j]
        return dp[n]
