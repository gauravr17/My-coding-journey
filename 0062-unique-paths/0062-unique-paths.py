class Solution(object):
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        # dp[j] represents the number of ways to reach column j in the current row
        dp = [1] * n
        
        for row in range(1, m):
            for col in range(1, n):
                dp[col] += dp[col - 1]
        
        return dp[-1]