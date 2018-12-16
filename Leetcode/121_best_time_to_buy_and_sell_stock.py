class Solution:
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if prices == []:
            return 0

        max_profit = 0

        l = prices[0]
        h = prices[0]

        for index, price in enumerate(prices):
            if price < l:
                l = price
                h = l
            if price > h:
                h = price
                tmp = h - l
                if tmp > max_profit:
                    max_profit = tmp

        return max_profit