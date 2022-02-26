class Solution:
    def findMin(self, nums: List[int]) -> int:

        ## Algorithm:
        ## https://www.youtube.com/watch?v=nIVW4P8b1VA
        ## Modified binary search.
        ## Invariance to idenify if we have rotated the array
        ## 1. lp value will alwayes be greater than rp value
        ## --> Will check if rotated or not
        ## 2. if roated by atleast half them the mid pointer will 
        ## always be greater than or equalt to the left-most(n=1)
        ## element. 
        ##  --> If we have rotated atleast half, we will search
        ##  the right portion else we will search the left portion

        lp, rp = 0, len(nums) - 1

        ## Very important: As out algorithm does not run for the
        ## non-ratated sorted array, we will take care of this by
        ## intializeing the result at left most value and update
        ##it after comparing
        res = nums[0]

        while lp <= rp:
            ## if already sorted then left most value will maybe
            ## the answer: Exception num_ = [2,3,4]
            ## Remember that our basic algorithm does not run on
            ## the non-roated sorted case
            if nums[lp] <= nums[rp]:
                res = min(res, nums[lp])
                break

            else:
                mp = (lp + rp) // 2
                ## As we ared discarding the mid point
                res = min(res, nums[mp])
                ## Search the right half
                if nums[mp] >= nums[lp]:
                    lp = mp + 1
                else:
                    rp = mp - 1
        return res
