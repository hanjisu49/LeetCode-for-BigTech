class Solution(object):
    def characterReplacement(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        l = 0
        count = {}
        length = 0
        
        for r in range(len(s)):
            count[s[r]] = 1 + count.get(s[r], 0)
            window = r - l + 1
            max_cnt = max(count.values())
            
            if window - max_cnt > k:
                count[s[l]] -= 1
                l += 1
                
            else:
                length = max(length, window)
        return length