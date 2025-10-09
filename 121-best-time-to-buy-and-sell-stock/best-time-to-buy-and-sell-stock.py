class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """

        max_profit = 0

        min_price = prices[0]
        
        for price in prices:
            min_price=min_price if min_price<=price else price
            max_profit=max_profit if max_profit>=price-min_price else price-min_price


        return max_profit



        