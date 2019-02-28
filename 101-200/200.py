class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid or not grid[0]:return 0
        def dfs(i,j):
            if 0<=i<len(grid) and 0<=j<len(grid[0]) and grid[i][j]=='1':
                grid[i][j]='0'
                dfs(i-1,j);dfs(i+1,j);dfs(i,j-1);dfs(i,j+1)
                return 1
            return 0
        return sum([dfs(i,j) for i in range(len(grid)) for j in range(len(grid[0]))])
