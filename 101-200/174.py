class Solution:
    def calculateMinimumHP(self, d):
        """
        :type dungeon: List[List[int]]
        :rtype: int
        """
        m,n=len(d),len(d[0])
        d[-1][-1]=max(1,1-d[-1][-1])
        for i in range(m-1,-1,-1):
            for j in range(n-1,-1,-1):
                if not(i==m-1 and j==n-1):
                    tmp=float('inf')
                    if i<m-1:
                        tmp=min(tmp,d[i+1][j])
                    if j<n-1:
                        tmp=min(tmp,d[i][j+1])
                    d[i][j]=max(1,tmp-d[i][j])
                    
        return d[0][0]
