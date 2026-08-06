class Solution(object):
    def hammingDistance(self, x, y):
        """
        :type x: int
        :type y: int
        :rtype: int
        """
        xor = x ^ y
        count = 0
        while xor:
            xor &= (xor - 1)
            count += 1
        return count