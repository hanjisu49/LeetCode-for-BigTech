class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """

        res = []
        nums.sort()
        # requires at least 3 numbers
        for i in range(len(nums) - 2):
            # go back up and run if next is same as the previous number
            if i > 0 and nums[i] == nums[i-1]:
                continue

            # the smallest after i = l, the largest number after i = r : i<l<r
            l, r = i + 1, len(nums) - 1

            # adjust l and r based on s=0
            while l < r:
                s = nums[i] + nums[l] + nums[r]
                
                if s < 0:
                    l += 1 
                elif s > 0:
                    r -= 1
                # add combination of s=0 to list res
                else:
                    res.append((nums[i], nums[l], nums[r]))
                    # +-1 again if the following values are equal to the previous values
                    while l < r and nums[l] == nums[l+1]:
                        l += 1
                    while l < r and nums[r] == nums[r-1]:
                        r -= 1
                    # If s is large, r is -1, and if s is small, l +1
                    l += 1 
                    r -= 1
        return res