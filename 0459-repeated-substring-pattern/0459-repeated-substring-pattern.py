class Solution(object):
    def repeatedSubstringPattern(self, s):
        n = len(s)
        for length in range(1, n // 2 + 1):
            if n % length == 0:
                candidate = s[:length]
                if candidate * (n // length) == s:
                    return True
        return False