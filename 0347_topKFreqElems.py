class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        # make dic with counting the number frequencies in nums
        dic = {}
        for i in nums:
            dic[i] = 1 + dic.get(i, 0)
        # print(dic)

        # create empty list by length of nums+1(because index start zero)
        freq = [[] for i in range(len(nums) + 1)]
        ## print(freq)
        # count가 index가 되도록 key값을 재배치
        for key, val in dic.items():
            freq[val].append(key)
        ## print(freq)

        # 빈 리스트 res에 freq리스트 역행으로 넣기 - 원소 개수가 k개가 될 때까지
        res = []
        for i in range(len(freq) - 1, 0 , -1):
            for n in freq[i]:
                res.append(n)
                if (len(res) == k):
                    ## print(res)
                    return res