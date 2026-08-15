class Solution(object):
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        m, n = len(s), len(p)
        
        # dp[i][j] = True if s[0:i] matches p[0:j]
        dp = [[False] * (n + 1) for _ in range(m + 1)]
        dp[0][0] = True
        
        # handle patterns like "a*", "a*b*", "a*b*c*" matching empty string
        for j in range(1, n + 1):
            if p[j - 1] == '*':
                dp[0][j] = dp[0][j - 2]
        
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if p[j - 1] == '*':
                    # zero occurrences of preceding element
                    dp[i][j] = dp[i][j - 2]
                    
                    # one or more occurrences, if preceding element matches s[i-1]
                    preceding = p[j - 2]
                    if preceding == '.' or preceding == s[i - 1]:
                        dp[i][j] = dp[i][j] or dp[i - 1][j]
                else:
                    if p[j - 1] == '.' or p[j - 1] == s[i - 1]:
                        dp[i][j] = dp[i - 1][j - 1]
        
        return dp[m][n]