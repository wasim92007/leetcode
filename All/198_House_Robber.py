class Solution:

    def rob(self, nums: List[int]) -> int:
        l = len(nums)

        if l <= 2:
            return max(nums)

        ## Algorithm: dp[i] will store the max till 0->i
        dp = [0]*l

        dp[0] = nums[0]
        dp[1] = max(nums[:2])

        for i in range(2, l):
            dp[i] = max(nums[i] + dp[i-2],   ## Max till 2nd last house + Curr house
                        dp[i-1])             ## We will skip this house: 

        return dp[l-1]
