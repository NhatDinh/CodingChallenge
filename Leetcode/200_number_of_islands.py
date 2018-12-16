class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        if grid == None or len(grid) == 0:
            return 0
        islands_count = 0
        nc = len(grid)
        nr = len(grid[0])
        for x in range(0, nc):
            for y in range(0, nr):
                if grid[x][y] == '1':
                    islands_count += 1
                    self._dfs( x, y, grid)
        return islands_count

    def _dfs(self, x, y, grid):
        nc = len(grid)
        nr = len(grid[0])
        if x < 0 or x >= nc or y < 0 or y >= nr or grid[x][y] == '0':
            return
        grid[x][y] = '0'
        self._dfs(x + 1, y, grid)
        self._dfs(x -1, y, grid)
        self._dfs(x, y + 1, grid)
        self._dfs(x, y - 1, grid)