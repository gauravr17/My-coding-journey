class Solution(object):
    def minPathSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        m, n = len(grid), len(grid[0])
        dp = [0] * n
        dp[0] = grid[0][0]
        
        # initialize first row (can only come from the left)
        for col in range(1, n):
            dp[col] = dp[col - 1] + grid[0][col]
        
        # process remaining rows
        for row in range(1, m):
            dp[0] += grid[row][0]  # first column can only come from above
            for col in range(1, n):
                dp[col] = min(dp[col], dp[col - 1]) + grid[row][col]
        
        return dp[-1]