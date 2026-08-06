class Solution(object):
    def islandPerimeter(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        rows = len(grid)
        cols = len(grid[0])
        perimeter = 0
        
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    perimeter += 4  # start by assuming all 4 sides are exposed
                    
                    # subtract 2 for each shared edge with a neighboring land cell
                    # (check only up and left to avoid double-counting shared edges)
                    if r > 0 and grid[r-1][c] == 1:
                        perimeter -= 2
                    if c > 0 and grid[r][c-1] == 1:
                        perimeter -= 2
        
        return perimeter