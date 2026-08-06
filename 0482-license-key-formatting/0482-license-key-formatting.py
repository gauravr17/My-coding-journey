class Solution(object):
    def licenseKeyFormatting(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: str
        """
        # Remove dashes and uppercase everything
        chars = s.replace("-", "").upper()
        
        # Build groups from the right (least significant end)
        result = []
        count = 0
        
        for i in range(len(chars) - 1, -1, -1):
            result.append(chars[i])
            count += 1
            if count == k and i != 0:
                result.append("-")
                count = 0
        
        return "".join(reversed(result))