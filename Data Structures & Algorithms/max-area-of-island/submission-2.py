class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        directions = [[0,1], [0,-1], [1,0], [-1,0]]
        ROWS, COLS = len(grid), len(grid[0])
        max_area = 0

        def bfs(r, c):
            q = deque()
            q.append((r, c))
            grid[r][c] = 0
            
            level = 1
            while q:
                row, col = q.popleft()

                for dr, dc in directions:
                    nr, nc = row + dr, col + dc
            
                    if (nr < 0 or nc < 0 or nr >= ROWS or nc >= COLS or grid[nr][nc] == 0):
                        continue
                        
                    q.append((nr, nc))
                    grid[nr][nc] = 0
                    level += 1
            return level
                    
        
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1:
                    max_area = max(max_area, bfs(r,c))
        return max_area
