class Solution:
    def countUnguarded(self, m: int, n: int, guards: List[List[int]], walls: List[List[int]]) -> int:
        grid = [[0] * n for _ in range(m)]  # 0: unoccupied, 1: guard, 2: wall, 3: guarded
        for r, c in guards:
            grid[r][c] = 1
        for r, c in walls:
            grid[r][c] = 2
        # Simulate guard vision
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]  # north, south, west, east
        for r, c in guards:
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                while 0 <= nr < m and 0 <= nc < n:
                    if grid[nr][nc] in (1, 2):  # Stop if a wall or guard is encountered
                        break
                    if grid[nr][nc] == 0:  # Mark as guarded
                        grid[nr][nc] = 3
                    nr += dr
                    nc += dc
        # Count unguarded cells
        unguarded_count = sum(grid[r][c] == 0 for r in range(m) for c in range(n))
        return unguarded_count
