class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        pos_buy, pos_sell = 0,0
        max_profit = 0
        for idx, price in enumerate(prices):
            if price < prices[pos_buy]:
                pos_buy = idx
            elif price >= prices[pos_sell]:
                pos_sell = idx

            if pos_buy >= pos_sell:
                pos_sell = idx
            max_profit = max(max_profit, prices[pos_sell] - prices[pos_buy])
            print(idx, price, ":", pos_buy, pos_sell)
        # if pos_buy > pos_sell:

        return max_profit