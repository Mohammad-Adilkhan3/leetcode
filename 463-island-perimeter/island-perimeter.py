class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        perimeter = 0
        row = len(grid)
        column = len(grid[0])
        for i in range(row):
            for j in range(column):
                if grid[i][j] == 0:
                    continue
                perimeter += 1 if i == 0 or grid[i - 1][j] == 0 else 0
                perimeter += 1 if i == row - 1 or grid[i + 1][j] == 0 else 0
                perimeter += 1 if j == 0 or grid[i][j - 1] == 0 else 0
                perimeter += 1 if j == column - 1 or grid[i][j + 1] == 0 else 0
        return perimeter
