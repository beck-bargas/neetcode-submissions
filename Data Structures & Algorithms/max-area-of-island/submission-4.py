class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        directions = [[0,1], [0,-1], [1,0], [-1,0]]
        ROWS, COLS = len(grid), len(grid[0])
        max_area = 0

        def bfs(r, c):
            q = deque()
            q.append((r,c))
            area = 0

            while q:
                for _ in range(len(q)):
                    r, c = q.popleft()
                    
                    if (r < 0 or c < 0 or r >= ROWS or c >= COLS or grid[r][c] == 0):
                        continue

                    area += 1
                    grid[r][c] = 0
                    for dr, dc in directions:
                        nr, nc = r + dr, c + dc
                        q.append((nr,nc))      
            return area

        for r in range(ROWS):
            for c in range(COLS):
                area = bfs(r,c)
                max_area = max(max_area, area)
        return max_area

        