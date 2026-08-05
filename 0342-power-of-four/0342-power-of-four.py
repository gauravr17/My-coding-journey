class Solution(object):
    def isPowerOfFour(self, n):
        """
        :type n: int
        :rtype: bool
        """
        if n <= 0:
            return False
        
        # must be a power of two (only one bit set)
        if n & (n - 1) != 0:
            return False
        
        # that one bit must be in an even position (0, 2, 4, 6, ...)
        # 0x55555555 has 1s at every even bit position (in 32-bit)
        return n & 0x55555555 != 0