class Solution(object):
    def summaryRanges(self, nums):
        """
        :type nums: List[int]
        :rtype: List[str]
        """
        result = []
        i = 0
        n = len(nums)
        
        while i < n:
            start = i
            # extend the range as long as consecutive numbers continue
            while i + 1 < n and nums[i + 1] == nums[i] + 1:
                i += 1
            # now i is the end of this range
            if start == i:
                result.append(str(nums[start]))
            else:
                result.append(str(nums[start]) + "->" + str(nums[i]))
            i += 1
        
        return result