class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        for b_idx, b in enumerate(prices):
            for s_idx in range(b_idx, len(prices)):
                max_profit = max(max_profit, prices[s_idx]-prices[b_idx])

        return max_profit