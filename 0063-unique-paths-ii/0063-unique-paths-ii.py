class Solution(object):
    def uniquePathsWithObstacles(self, obstacleGrid):
        """
        :type obstacleGrid: List[List[int]]
        :rtype: int
        """
        if not obstacleGrid or obstacleGrid[0][0] == 1:
            return 0
        
        n = len(obstacleGrid[0])
        dp = [0] * n
        dp[0] = 1  # starting cell, if not blocked
        
        for row in obstacleGrid:
            for col in range(n):
                if row[col] == 1:
                    dp[col] = 0  # obstacle blocks this cell entirely
                elif col > 0:
                    dp[col] += dp[col - 1]
                # if col == 0 and no obstacle, dp[0] stays as-is (carried from above)
        
        return dp[-1]