class Solution(object):
    def maxProfit(self, prices):
        max_price = max(prices)
        min_price = min(prices)
        arraylen = len(prices)
        profit = 0
        vally = prices[0]
        peak = prices[0]
        i = 0
        j = 1
        i_value = i
        j_value = j
        max_profit = 0
        while i < arraylen-1:
            i = i + 1
            if(prices[i] <= vally):
                vally = prices[i]
                i_value = i
                j = j + 1
            else:
                if(prices[j] >= peak):
                    peak = prices[j]
                    j_value = j
                    j = j + 1
        if(j_value > i_value):
            max_profit = (prices[j_value] - prices[i_value])
        return(max_profit, vally, peak, i_value, j_value)
sln = Solution()
result = sln.maxProfit([9, 1, 5, 3, 6, 1, 2])
print(result)