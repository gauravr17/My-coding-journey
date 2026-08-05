from collections import Counter

class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        counts = Counter(s)
        
        for i, char in enumerate(s):
            if counts[char] == 1:
                return i
        
        return -1