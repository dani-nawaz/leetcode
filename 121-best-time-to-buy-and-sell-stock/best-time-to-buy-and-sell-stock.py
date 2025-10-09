class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """

        L = 0
        R = 1
        maxP = 0

        while R < len(prices):
            if prices[L] < prices[R]:
                profit = prices[R] - prices[L]
                maxP = max(maxP, profit)
            else:
                L = R
            R+=1

        return maxP