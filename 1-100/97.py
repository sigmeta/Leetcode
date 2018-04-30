class Solution0: #递归方法超时
    def isInterleave(self, s1, s2, s3):
        """
        :type s1: str
        :type s2: str
        :type s3: str
        :rtype: bool
        """
        if len(s1)+len(s2)!=len(s3):
            return False
        if len(s1)==0 and s2==s3 or len(s2)==0 and s1==s3:
            return True
        elif len(s1)==0 or len(s2)==0:
            return False
        if s1[0]==s3[0] and self.isInterleave(s1[1:],s2,s3[1:]):
            return True
        elif s2[0]==s3[0] and self.isInterleave(s1,s2[1:],s3[1:]):
            return True
        else:
            return False
            
  class Solution:    #动态规划通过
    def isInterleave(self, s1, s2, s3):
        """
        :type s1: str
        :type s2: str
        :type s3: str
        :rtype: bool
        """        
        if len(s1)+len(s2)!=len(s3):
            return False
        m=len(s1);n=len(s2)
        dp=[[False for j in range(n+1)] for i in range(m+1)]
        dp[0][0]=True
        for i in range(m):
            if s1[i]==s3[i]:
                dp[i+1][0]=True
            else:
                break
        for i in range(n):
            if s2[i]==s3[i]:
                dp[0][i+1]=True
            else:
                break
        for i in range(m):
            for j in range(n):
                if i+j==m+n:
                    dp[i+1][j+1]=dp[i+1][j] or dp[i][j+1]
                    break
                if dp[i+1][j] and s2[j]==s3[i+j+1]:
                    dp[i+1][j+1]=True
                elif dp[i][j+1] and s1[i]==s3[i+j+1]:
                    dp[i+1][j+1]=True
        return dp[m][n]
