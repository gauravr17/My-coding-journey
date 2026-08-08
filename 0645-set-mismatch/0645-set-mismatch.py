class Solution(object):
    def findErrorNums(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        n = len(nums)
        seen = set()
        duplicate = -1
        actual_sum = 0
        
        for num in nums:
            if num in seen:
                duplicate = num
            seen.add(num)
            actual_sum += num
        
        # Expected sum of 1..n
        expected_sum = n * (n + 1) // 2
        
        # actual_sum currently includes duplicate twice and misses the missing number
        # actual_sum - duplicate + missing = expected_sum
        missing = expected_sum - (actual_sum - duplicate)
        
        return [duplicate, missing]