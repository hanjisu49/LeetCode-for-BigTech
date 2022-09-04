# when prices =[9  2  5  8  6  1  11  12  10],
# let's (buy, sell) = profit
# (9,2) = -7 < 0
# (2,5) = 3  > 0 !positive
# save 3 in profit. keep L=2 and move only R one space
# L is changed if the number is smaller than the current L

# (2,8) = 6 > 0 (6 is bigger than 3, so change it to 6 and save it) 
# (2,6) = 4 > 0 (keep 6)
# (2,1) = -1 < 0 (keep 6 and convert L to current R)

class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        L = 0   # buy
        R = 1   # sell
        max_profit = 0
        
        while R < len(prices):
            profit = prices[R] - prices[L]
            if profit < 0:
                L = R
                R += 1
            else:
                R += 1
            max_profit = max(max_profit, profit)
        return max_profit

# final
## 'R += 1' can be pulled out because it fits in both the if and else phrases.
class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        L = 0   # buy
        R = 1   # sell
        max_profit = 0
        
        while R < len(prices):
            profit = prices[R] - prices[L]
            if profit < 0:
                L = R
            R += 1
            max_profit = max(max_profit, profit)
        return max_profit