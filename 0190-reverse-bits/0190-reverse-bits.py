class Solution(object):
    def reverseBits(self, n):
        """
        :type n: int
        :rtype: int
        """
        result = 0
        for i in range(32):
            bit = (n >> i) & 1
            result = result | (bit << (31 - i))
        return result