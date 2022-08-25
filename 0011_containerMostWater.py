class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        L = 0
        R = len(height)-1
        res = 0
        
        while L < R:
            area = (R-L)*min(height[R], height[L])
            res = max(res, area)
            
            if height[L] > height[R]:
                R -= 1
            elif height[L] < height[R]:
                L += 1
            else:
                R -= 1
                L += 1
                     
        return res 