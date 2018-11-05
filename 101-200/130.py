class Solution:
    def solve(self, board):
        """
        :type board: List[List[str]]
        :rtype: void Do not return anything, modify board in-place instead.
        """
        if not board:
            return
        def search(row,col):
            if row==-1 or row==len(board):
                return 
            if col==-1 or col==len(board[0]):
                return
            if board[row][col]=='O':
                board[row][col]='A'
                search(row-1,col)
                search(row,col-1)
                search(row+1,col)
                search(row,col+1)
            else:
                return
        for i in range(len(board)):
            search(i,0)
            search(i,len(board[0])-1)
        for i in range(1,len(board[0])-1):
            search(0,i)
            search(len(board)-1,i)
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j]=='A':
                    board[i][j]='O'
                elif board[i][j]=='O':
                    board[i][j]='X'
        return
