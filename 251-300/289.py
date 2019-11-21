class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        # 0:0->0, 1:1->1, -1:0->1, -2:1->0
        if not board:
            return None
        m=len(board)
        n=len(board[0])
        for i in range(m):
            for j in range(n):
                count=0
                for r in range(i-1,i+2):
                    for c in range(j-1,j+2):
                        if r<0 or r>=m or c<0 or c>=n or r==i and c==j:
                            continue
                        elif board[r][c]==-1:
                            continue
                        elif board[r][c]==-2:
                            count+=1
                        else:
                            count+=board[r][c]
                if board[i][j]==0 and count==3:
                    board[i][j]=-1
                elif board[i][j]==1 and (count<2 or count>3):
                    board[i][j]=-2
        for i in range(m):
            for j in range(n):
                if board[i][j]==-1:
                    board[i][j]=1
                elif board[i][j]==-2:
                    board[i][j]=0
        return None


