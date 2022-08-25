class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        # start at both ends
        L = 0
        R = len(height)-1
        res = 0
        
        # consider conditions that can never have a maximum
        ## bottom length continues to decrease, key is height
        while L < R:
            area = (R-L)*min(height[R], height[L])
            res = max(res, area)
            
            # move the small y-axis value inward
            if height[L] > height[R]:
                R -= 1
            elif height[L] < height[R]:
                L += 1
            else:
                R -= 1
                L += 1
                     
        return res 