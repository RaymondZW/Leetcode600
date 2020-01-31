from typing import List


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        # DFS
        res = [0]
        if not grid or not grid[0]:
            return res[0]
        m = len(grid)
        n = len(grid[0])
        def floodfill(i, j):
            if i < 0 or i == m or j < 0 or j == n or grid[i][j] != '1':
                return

            grid[i][j] = '0'
            floodfill(i + 1, j)
            floodfill(i - 1, j)
            floodfill(i, j + 1)
            floodfill(i, j - 1)
            return

        for i in range(m):
            for j in range(n):
                if grid[i][j] == '1':
                    res[0] += 1
                    floodfill(i, j)
        return res[0]


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        # BFS
        # We will use a queue in the floodfill function
        if not grid or not grid[0]:
            return 0
        m = len(grid)
        n = len(grid[0])

        res = [0]
        def floodfill(i, j):
            if i < 0 or i == n or j < 0 or j == m or grid[i][j] != '1':
                return

            # q =

        for i in range(m):
            for j in range(n):
                if grid[i][j] == '1':
                    res[0] += 1
                    floodfill(i, j)

