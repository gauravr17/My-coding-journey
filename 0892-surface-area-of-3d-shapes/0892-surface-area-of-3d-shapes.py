class Solution(object):
    def surfaceArea(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        n = len(grid)
        area = 0
        
        for i in range(n):
            for j in range(n):
                v = grid[i][j]
                if v > 0:
                    area += 2 + 4 * v  # top+bottom, plus 4 sides
                    
                    # subtract overlap with the neighbor above (i-1, j)
                    if i > 0:
                        area -= 2 * min(v, grid[i-1][j])
                    # subtract overlap with the neighbor to the left (i, j-1)
                    if j > 0:
                        area -= 2 * min(v, grid[i][j-1])
        
        return area