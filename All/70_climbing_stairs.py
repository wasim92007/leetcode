class Solution:
    def climbStairs(self, n: int) -> int:
        ## We will use dynamic problem for this.
        ## Let us initialize the base case for 0,1 step as 1
        ##
        dp = [0]*(n+1)
        dp[0] = 1
        dp[1] = 1
        
        ## We will populate the array till n+1
        for i in range(2,n+1):
            ## Basically we can use the below recurrence equation
            dp[i] = dp[i-1] + dp[i-2]
            
        return dp[n]
        
