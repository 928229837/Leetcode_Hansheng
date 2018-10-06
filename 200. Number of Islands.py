# Given a 2d grid map of '1's (land) and '0's (water), count the number of islands. An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. You may assume all four edges of the grid are all surrounded by water.
#
# Example 1:
#
# Input:
# 11110
# 11010
# 11000
# 00000
#
# Output: 1
# Example 2:
#
# Input:
# 11000
# 11000
# 00100
# 00011
#
# Output: 3

"""
72 ms quick for type
"""


class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        if not grid:
            return 0
        res = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == "1":
                    res += 1
                    self.explore(grid, i, j)
        return res

    def explore(self, grid, i, j):
        if i < 0 or j < 0 or i >= len(grid) or j >= len(grid[0]) or grid[i][j] != "1":
            return
        grid[i][j] = 0
        self.explore(grid, i + 1, j)
        self.explore(grid, i, j + 1)
        self.explore(grid, i - 1, j)
        self.explore(grid, i, j - 1)


"""
56 ms longer type
"""


class Solution(object):

    def explore(self, grid, i, j):
        if (i + 1 < len(grid) and grid[i + 1][j] == "1"):
            grid[i + 1][j] = "0"
            grid = self.explore(grid, i + 1, j)
        if (j + 1 < len(grid[i]) and grid[i][j + 1] == "1"):
            grid[i][j + 1] = "0"
            grid = self.explore(grid, i, j + 1)
        if (i > 0 and grid[i - 1][j] == "1"):
            grid[i - 1][j] = "0"
            grid = self.explore(grid, i - 1, j)
        if (j > 0 and grid[i][j - 1] == "1"):
            grid[i][j - 1] = "0"
            grid = self.explore(grid, i, j - 1)
        return grid

    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        res = 0
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if (grid[i][j] == '1'):
                    res += 1
                    grid[i][j] = '0'
                    grid = self.explore(grid, i, j)
        return res
