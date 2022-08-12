class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        
        dic = {}
        for w in strs:
            key = tuple(sorted(w))
            dic[key] = dic.get(key, []) + [w]
        return list(dic.values())