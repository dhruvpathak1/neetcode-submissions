class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        i = 0
        j = 1
        buy = -1
        sell = -1
        profit = -1
        diff = 0

        print("Len:", len(prices))
        
        while i <= (len(prices)-2):
            print(i,j)

            diff = prices[j] - prices[i]
            if diff > profit:
                # print(i,j)
                profit = diff
                buy = i
                sell = j
            else:
                j += 1
            
            if j == len(prices):
                i += 1
                j = i + 1

        
        if profit == -1:
            return 0
        else:
            return profit
        
        