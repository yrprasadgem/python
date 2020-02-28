class Solution(object):
    def maxProfit(self, prices):
        """

        """
        array_len = len(prices)
        i = 0
        j = 1
        max_profit = 0
        peak = 0
        latest_i = i
        latest_j = i
        max_profit = 0
        prifit = 0
        if(array_len > 0):
            vally = prices[0]
            for i in range(array_len-1):
                j = i + 1
                if(prices[i] <= vally):
                    vally = prices[i]
                    latest_i = i
                    if(prices[j] >= peak):
                        peak = prices[j]
                        latest_j = j
                    else:
                        if(latest_j > latest_i):
                            profit = peak - vally
                        else:
                            profit = max_profit
                            vally = peak
                else:
                    if(prices[j] >= peak):
                        peak = prices[j]
                        latest_j = j
                    else:
                        if(latest_j > latest_i):
                            profit = peak - vally
                        else:
                            profit = max_profit
                            vally = peak
                if(latest_j > latest_i):
                    profit = peak - vally
                else:
                    profit = max_profit
                    vally = peak
                profit = peak - vally
                if(profit >= max_profit):
                    max_profit = profit
                i = i + 1
        else:
            max_profit = 0
        return(max_profit)
sln = Solution()
result = sln.maxProfit([])
print(result)