class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        highest_profit = 0
        left = 0
        right = 1

        while right < len(prices):

            if prices[left] > prices[right] or prices[left] == prices[right]:

                left += 1
                right += 1

            elif prices[left] < prices[right]:

                while right < len(prices) and prices[left] < prices[right]:

                    current_profit = prices[right] - prices[left]

                    if current_profit > highest_profit:

                        highest_profit = current_profit

                    right += 1
                
                left += 1
                right = left + 1

        return highest_profit

        