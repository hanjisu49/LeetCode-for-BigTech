class Solution(object):
    def checkInclusion(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: bool
        """
        if len(s1) > len(s2): return False
        
        # create a list of lengths from A to Z (A~Z = 26)
        s1_cnt, s2_cnt = [0] * 26, [0] * 26

        # display the spellings included in s1 and s2 in the list (according to the length of s1)
        # # use ASCII to +1 the number of letters in the corresponding alphabet
        for i in range(len(s1)):
            s1_cnt[ord(s1[i]) - ord('a')] += 1
            s2_cnt[ord(s2[i]) - ord('a')] += 1

        # count matching : if it's the same +1, or +0
        matches = 0
        for i in range(26):
            matches += (1 if s1_cnt[i] == s2_cnt[i] else 0)

        l = 0
        for r in range(len(s1), len(s2)):
            if matches == 26: return True

            index = ord(s2[r]) - ord('a')   # index presented with ASCII
            s2_cnt[index] += 1  # fill in the back of the s2 list
            if s1_cnt[index] == s2_cnt[index]:
                matches += 1
            elif s1_cnt[index] + 1 == s2_cnt[index]:
                matches -= 1

            # delete the front part info as the sliding window
            index = ord(s2[l]) - ord('a')
            s2_cnt[index] -= 1
            if s1_cnt[index] == s2_cnt[index]:
                matches += 1
            elif s1_cnt[index] - 1 == s2_cnt[index]:
                matches -= 1
            l += 1
        return matches == 26    # return False


        # # when import counter lib.
        # from collections import Counter
        # cntr, w, match = Counter(s1), len(s1), 0     

        # for i in range(len(s2)):
        # 	if s2[i] in cntr:
        # 		if not cntr[s2[i]]: match -= 1
        # 		cntr[s2[i]] -= 1
        # 		if not cntr[s2[i]]: match += 1

        # 	if i >= w and s2[i-w] in cntr:
        # 		if not cntr[s2[i-w]]: match -= 1
        # 		cntr[s2[i-w]] += 1
        # 		if not cntr[s2[i-w]]: match += 1

        # 	if match == len(cntr):
        # 		return True

        # return False


        # # time limit exceeded case : 1st try
        # for l in range (len(s2)-len(s1)+1):  
        #     if sorted(s2[l:l+len(s1)]) == sorted(s1):
        #         return True
        
        # return False