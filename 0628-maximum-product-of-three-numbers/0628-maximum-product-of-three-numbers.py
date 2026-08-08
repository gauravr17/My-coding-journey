class Solution(object):
    def maximumProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        n = len(nums)

        # Candidate 1: three largest numbers
        candidate1 = nums[n-1] * nums[n-2] * nums[n-3]

        # Candidate 2: two smallest (possibly negative) * largest number
        candidate2 = nums[0] * nums[1] * nums[n-1]

        return max(candidate1, candidate2)