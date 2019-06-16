class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        m=0
        c=[[0]*len(matrix[0]) for _ in range(len(matrix))]
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if i==0 or j==0:
                    c[i][j]=int(matrix[i][j])
                elif matrix[i][j]=='1':
                    c[i][j]=min(c[i-1][j-1],c[i-1][j],c[i][j-1])+1
                m=max(m,c[i][j])
        return m**2
