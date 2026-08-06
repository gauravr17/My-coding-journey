from collections import Counter

class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: int
        """
        counts = Counter(s)
        length = 0
        has_odd = False
        
        for char, count in counts.items():
            length += (count // 2) * 2  # use as many pairs as possible
            if count % 2 == 1:
                has_odd = True
        
        if has_odd:
            length += 1  # one leftover odd character can sit in the middle
        
        return length