class Solution:
    def rob(self, nums: List[int]) -> int:

        ## Get the length first
        l = len(nums)

        ## In case of circular for l <=3
        ## We can only rob one house
        if l <= 3:
            return max(nums)

        ## Algorithm: We will break the circular dependency
        ## by taking two over-lapping array and getting the max
        ## of both
        ## https://www.youtube.com/watch?v=rWAJCfYYOvM
        return max(self.rob_non_circular(nums=nums[:-1]), self.rob_non_circular(nums=nums[1:]))

    def rob_non_circular(self, nums: List[int]) -> int:
        ## Will be used to keep track of the max value till
        ## 2nd last houst and last house.
        till_2nd_last, till_last = 0, 0

        ## Algorithm: The max value at the current house will
        ## be maximum of till_2nd_last plus value at current 
        ## house, till_last house
        for num in nums:
            till_curr = max(till_2nd_last + num, till_last)

            ## Shift one to the rigt for next iteration
            till_2nd_last, till_last = till_last, till_curr

        ## At the end of the loop the till_last will be the till_curr
        return till_last
