class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums.sort()
        n = len(nums)
        result = []
        
        for i in range(n - 2):
            # skip duplicate values for the first number
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            
            # small optimization: if smallest possible sum > 0, no triplet works from here on
            if nums[i] > 0:
                break
            
            left, right = i + 1, n - 1
            target = -nums[i]
            
            while left < right:
                current_sum = nums[left] + nums[right]
                
                if current_sum == target:
                    result.append([nums[i], nums[left], nums[right]])
                    left += 1
                    right -= 1
                    
                    # skip duplicates for the second number
                    while left < right and nums[left] == nums[left - 1]:
                        left += 1
                    # skip duplicates for the third number
                    while left < right and nums[right] == nums[right + 1]:
                        right -= 1
                
                elif current_sum < target:
                    left += 1
                else:
                    right -= 1
        
        return result