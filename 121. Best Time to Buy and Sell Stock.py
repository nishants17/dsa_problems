# Input: prices = [7,1,5,3,6,4]
# Output: 5 (Find Max Profit)
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l, r = 0, 1
        maxProfit = 0
        while r < len(prices):
            if prices[l] >= prices[r]:
                l = r
                r+=1
            elif prices[l] < prices[r]:
                maxProfit = max(maxProfit, prices[r] - prices[l])
                r+=1
        return maxProfit
        
