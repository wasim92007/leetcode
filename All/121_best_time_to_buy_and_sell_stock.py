class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        
        ## https://www.youtube.com/watch?v=1pkOgXD63yU
        ## Two pointer solution
        # Initializing the l, r pointer and max_profit
        l, r = 0, 1
        max_profit = 0
        
        ## We will increment the right poiter till len(prices)
        while r < len(prices):
            ## Profitable?
            if prices[l] < prices[r]:
                ## Calculate current profit
                curr_profit = prices[r] - prices[l]
                ## Update max profit
                max_profit = max(max_profit, curr_profit)
            else:
                ## We we find a even lower price, we will set the cost to that
                l = r
            ## We will increment the right pointer every iteration
            r += 1
            
        return max_profit
                
        
        ## Solution 1: Slow solution
        max_profit = 0
        curr_max = 0
        
        for i in range(len(prices) - 1):
            curr_max = max(curr_max + prices[i+1] - prices[i], 0)
            max_profit = max(curr_max, max_profit)
            
        return max_profit
