class Solution:
    def trap(self, height: List[int]) -> int:
        ## Algorithm: Two-pointer outward in greedy
        trapped_water = 0
        min_level = 0
        lp, rp = 0, len(height) - 1

        while lp != rp:
            ## If the min_level for trapping is higher that the lp and rp height
            ## Add the difference.
            trapped_water += max(0, min_level-height[lp]) + max(0, min_level-height[rp])
            ## Update min level for trapping to a higher both side bounded value
            min_level = max(min_level, min(height[lp], height[rp]))
            ## Greedily try to increase the height
            if height[lp] < height[rp]:
                lp += 1
            else:
                rp -= 1
                

        return trapped_water  
