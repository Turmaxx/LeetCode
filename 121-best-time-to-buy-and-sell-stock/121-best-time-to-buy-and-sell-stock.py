class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        left, right,max_profit = 0, 1, 0
        while right < len(prices):
            currentProfit = prices[right] - prices[left]
            if prices[left] < prices[right]:
                max_profit = max(currentProfit,max_profit)
            else:
                left = right
            right += 1
        return max_profit