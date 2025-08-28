class Solution:
    def sortMatrix(self, grid: List[List[int]]) -> List[List[int]]:
        n = len(grid)
        d = {}
        for i in range(n):
            for j in range(n):
                key = i - j
                if key not in d:
                    d[key] = []
                d[key].append(grid[i][j])
        for key in d:
            if key >= 0:
                d[key].sort(reverse=True)  
            else:
                d[key].sort() 
        for i in range(n):
            for j in range(n):
                key = i - j
                grid[i][j] = d[key].pop(0)
        return grid