class Solution:
    def maxArea(self, height: List[int]) -> int:

        ### Algorithm: Brite force solution
        ### Time Limit Exceeded Error
        ### Check every pair of container
        #area = 0
        #for lp in range(len(height)):
        #    ## Set rp to the immediate next point
        #    rp = lp + 1
        #    ## As long as rp is in bound
        #    for rp in range(lp+1,len(height)):
        #        ## Get the new area
        #        new_area = (rp-lp) * min(height[lp], height[rp])
        #        ## Update the old are if required
        #        if new_area > area:
        #            area = new_area

        #return area

        ## Alogorithm
        ## https://www.youtube.com/watch?v=UuiTKBwPgAo
        ## Kind of greedy algorithm.
        ## Start with left and right pointer initialized to the
        ## Extreme left and right and try to maximize the height
        lp, rp = 0, len(height) - 1
        area = 0
        while lp != rp:
            ## Update new area
            area = max(area, (rp-lp)*min(height[lp], height[rp]))
            if height[lp] < height[rp]:
                lp += 1
            else:
                rp -= 1

        return area
