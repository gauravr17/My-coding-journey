class Solution(object):
    def toHex(self, num):
        """
        :type num: int
        :rtype: str
        """
        if num == 0:
            return "0"
        
        hex_digits = "0123456789abcdef"
        result = []
        
        # Mask to 32 bits to handle negative numbers via two's complement
        num &= 0xFFFFFFFF
        
        while num > 0:
            result.append(hex_digits[num & 0xF])
            num >>= 4
        
        return "".join(reversed(result))