class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if len(s) != len(t):
            return False
        else:
            s = list(s)
            t = list(t)
            return sorted(s) == sorted(t)

# other best answers - use dictionary
def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        dic = {}
        for i in s:
            if i not in dic:
                dic[i] = 1
            else:
                dic[i] += 1
        
        for j in t:
            if j not in dic:
                return False
            else:
                dic[j] -= 1
        
        for val in dic.values():
            if val != 0:
                return False
        
        return True

# python module - collections.Counter 이용 (from collections import Counter 필요) 
def isAnagram1(self, s, t):
    return collections.Counter(s) == collections.Counter(t)