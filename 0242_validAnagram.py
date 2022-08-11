class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        temp_s = list(s).sort()
        temp_t = list(t).sort()
        
        if temp_s == temp_t:
            return True
        else:
            return False