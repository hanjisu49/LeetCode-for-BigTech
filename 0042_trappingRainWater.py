class Solution:
    def trap(self, height):
        # rainwater cannot accumulate when there are less than two elements
        if len(height) <= 2: return 0
        
        # rainwater cannot be collected at the beginning and the end
        ptr_l, ptr_r = 1, len(height) - 2
        max_l, max_r = height[0], height[-1]
        res = 0
        
        # same way as '0011_containerMostWater'
        ## repeat until 'ptr_l' is less than or equal to 'ptr_r'
        while ptr_l <= ptr_r:
            if max_l < height[ptr_l]: max_l = height[ptr_l]
            if max_r < height[ptr_r]: max_r = height[ptr_r] 
            
            # move pointer and compute, save res
            if max_l < max_r:
                res += max_l - height[ptr_l]
                ptr_l += 1
            else:
                res += max_r - height[ptr_r]
                ptr_r -= 1
        return res