class Solution(object):
    def uniquePathsIII(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        self.rows = len(grid)
        self.cols =  len(grid[0])
        startrow,startcol = 0,0
        e=0
        for r in range(self.rows):
            for c in range(self.cols):
                if grid[r][c]==0:
                    e = e+1
                if grid[r][c]==1:
                    startrow,startcol = r,c
        return self.dfs(grid,startrow,startcol,e)
    def dfs(self,grid,r,c,e):
        if r<0 or r>=self.rows or c<0 or c>=self.cols:
            return 0
        if grid[r][c]==-1:
            return 0
        if grid[r][c]==2:
            return 1 if e == 0 else 0
        temp = grid[r][c]
        if temp ==0:
            e=e-1
        grid[r][c]=-1
        paths=(self.dfs(grid,r+1,c,e)+self.dfs(grid,r-1,c,e)+self.dfs(grid,r,c+1,e)+self.dfs(grid,r,c-1,e))
        grid[r][c]=temp
        return paths        