#
# @lc app=leetcode id=55 lang=python3
#
# [55] Jump Game
#
# https://leetcode.com/problems/jump-game/description/
#
# algorithms
# Medium (37.41%)
# Likes:    9852
# Dislikes: 567
# Total Accepted:    906.1K
# Total Submissions: 2.4M
# Testcase Example:  '[2,3,1,1,4]'
#
# You are given an integer array nums. You are initially positioned at the
# array's first index, and each element in the array represents your maximum
# jump length at that position.
# 
# Return true if you can reach the last index, or false otherwise.
# 
# 
# Example 1:
# 
# 
# Input: nums = [2,3,1,1,4]
# Output: true
# Explanation: Jump 1 step from index 0 to 1, then 3 steps to the last index.
# 
# 
# Example 2:
# 
# 
# Input: nums = [3,2,1,0,4]
# Output: false
# Explanation: You will always arrive at index 3 no matter what. Its maximum
# jump length is 0, which makes it impossible to reach the last index.
# 
# 
# 
# Constraints:
# 
# 
# 1 <= nums.length <= 10^4
# 0 <= nums[i] <= 10^5
# 
# 
#

# @lc code=start
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

        
# @lc code=end

