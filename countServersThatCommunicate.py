class Solution:
    def countServers(self, grid: List[List[int]]) -> int:
        n,m=len(grid),len(grid[0])
        tot=0
        r,c=[0]*n,[0]*m
        for i in range(n):
            for j in range(m):
                if grid[i][j]==1:
                    r[i]+=1
                    c[j]+=1
        for i in range(n):
            for j in range(m):
                if grid[i][j]==1 and (r[i]>1 or c[j]>1):
                    tot+=1
        return tot
            
