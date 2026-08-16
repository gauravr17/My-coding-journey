class Solution(object):
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        nums.sort()
        n = len(nums)
        result = []
        
        for i in range(n - 3):
            # skip duplicate values for the first number
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            
            for j in range(i + 1, n - 2):
                # skip duplicate values for the second number
                if j > i + 1 and nums[j] == nums[j - 1]:
                    continue
                
                left, right = j + 1, n - 1
                remaining = target - nums[i] - nums[j]
                
                while left < right:
                    current_sum = nums[left] + nums[right]
                    
                    if current_sum == remaining:
                        result.append([nums[i], nums[j], nums[left], nums[right]])
                        left += 1
                        right -= 1
                        
                        # skip duplicates for third number
                        while left < right and nums[left] == nums[left - 1]:
                            left += 1
                        # skip duplicates for fourth number
                        while left < right and nums[right] == nums[right + 1]:
                            right -= 1
                    
                    elif current_sum < remaining:
                        left += 1
                    else:
                        right -= 1
        
        return result