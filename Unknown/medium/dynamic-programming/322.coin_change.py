#
# @lc app=leetcode id=322 lang=python3
#
# [322] Coin Change
#
# https://leetcode.com/problems/coin-change/description/
#
# algorithms
# Medium (39.66%)
# Likes:    10265
# Dislikes: 250
# Total Accepted:    907.4K
# Total Submissions: 2.3M
# Testcase Example:  '[1,2,5]\n11'
#
# You are given an integer array coins representing coins of different
# denominations and an integer amount representing a total amount of money.
# 
# Return the fewest number of coins that you need to make up that amount. If
# that amount of money cannot be made up by any combination of the coins,
# return -1.
# 
# You may assume that you have an infinite number of each kind of coin.
# 
# 
# Example 1:
# 
# 
# Input: coins = [1,2,5], amount = 11
# Output: 3
# Explanation: 11 = 5 + 5 + 1
# 
# 
# Example 2:
# 
# 
# Input: coins = [2], amount = 3
# Output: -1
# 
# 
# Example 3:
# 
# 
# Input: coins = [1], amount = 0
# Output: 0
# 
# 
# 
# Constraints:
# 
# 
# 1 <= coins.length <= 12
# 1 <= coins[i] <= 2^31 - 1
# 0 <= amount <= 10^4
# 
# 
#

# @lc code=start
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [amount+1]*(amount+1)

        ## Base case
        dp[0] = 0

        ## We will fill-up the dp array
        for a in range(1, amount+1):
            ## Iterate for all the coins
            for c in coins:
                #print(f'a:{a}, c:{c}, dp:{dp}')
                ## Onlu compute if we can make a change
                ## amount is greater than equal to coin value
                if a - c >= 0:
                    dp[a] = min(dp[a], 1 + dp[a-c])
                    #print(f'a:{a}, c:{c}, dp:{dp}')
                
        ## Return -1 if we still have the default value
        return dp[amount] if dp[amount] != amount + 1 else -1
        
# @lc code=end

