class Solution(object):
    def isSubsequence(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        i = 0  # pointer for s
        
        for char in t:
            if i < len(s) and char == s[i]:
                i += 1
        
        return i == len(s)