class Solution(object):
    def kInversePairs(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: int
        """
        MOD = 10**9 + 7

        # Max possible inverse pairs for n elements is n*(n-1)/2
        if k > n * (n - 1) // 2:
            return 0

        # dp[j] = number of permutations of current length with j inverse pairs
        # Start representing "permutations of 0 elements": dp[0] = 1
        dp = [0] * (k + 1)
        dp[0] = 1

        for i in range(1, n + 1):
            new_dp = [0] * (k + 1)
            new_dp[0] = 1  # 0 inverse pairs always has exactly 1 way
            for j in range(1, k + 1):
                # dp[i][j] = dp[i][j-1] + dp[i-1][j] - dp[i-1][j-i]
                new_dp[j] = (new_dp[j - 1] + dp[j]) % MOD
                if j - i >= 0:
                    new_dp[j] = (new_dp[j] - dp[j - i]) % MOD
            dp = new_dp

        return dp[k] % MOD