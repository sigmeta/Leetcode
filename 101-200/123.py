import sys
class Solution:
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        buy1=buy2=sys.maxsize;sell1=sell2=0
        for i in range(len(prices)):
            buy1=min(buy1,prices[i])
            sell1=max(sell1,prices[i]-buy1)
            buy2=min(buy2,prices[i]-sell1)
            sell2=max(sell2,prices[i]-buy2)
        return sell2
        
