class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        
        """
        nums = list(set(nums))
        nums = sorted(nums)

        maximum = 0
        local_max = 1

        if len(nums) != 0:
            for i in range(1,len(nums)):
                if nums[i] == nums[i-1]+1:
                    local_max +=1
                else:
                    maximum = max(maximum, local_max)
                    local_max = 1
            return max(maximum, local_max)
        else:
            return 0