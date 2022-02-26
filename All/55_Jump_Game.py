class Solution:
    def canJump(self, nums: List[int]) -> bool:
        
        #### Algorithm: Does not work
        ####            leads to Time Limit Exceeded
        #### dp[i] will be true if we can go to the last element
        #### from the i'th position, otherwise it will be false
        #### for nums[i] = 2, dp[i] will be true if dp[i+1] OR
        #### dp[i+2] are

        #### Get length
        ##l = len(nums)

        #### Create dp
        ##dp = [False]*l

        #### Base case
        ##dp[l-1] = True

        ##for i in range(l-2,-1,-1):
        ##    if nums[i] == 0:
        ##        dp[i] = False
        ##    else:
        ##        for j in range(nums[i]+1):
        ##            ## Optimization to skip early when we
        ##            ## know that we can take that path
        ##            if not dp[i]:
        ##                dp[i] = dp[i] or dp[i+j]
        ##            else:
        ##                break

        ##return dp[0]

        ## Algorithm: We will start from left and keep bringing
        ## our goal post closer
        ## https://www.youtube.com/watch?v=Yan0cv2cLy8

        ## Get length
        l = len(nums)
        
        ## We will keep bringing the goal position closer
        goal_position = l-1

        for i in range(l-2,-1,-1):
            if i + nums[i] >= goal_position:
                goal_position = i

        return True if goal_position == 0 else False
