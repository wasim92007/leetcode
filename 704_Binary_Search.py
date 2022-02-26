class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l,r = 0, len(nums) - 1

        ## Alternative faster solution: Tries to return the
        ## left point
        while l < r:
            m = l + (r-l+1)//2  ## Mid will co-inside with r for n =2
            #print(f'l:{l}, m:{m}, r:{r}')

            if target < nums[m]:
                r = m -1
            else:
                l = m
        
        return l if nums[l] == target else -1



        ## My First Solution: I try to return the mid point
        ## We will searchin the range
        ## l = r: Takes care of single element array
        while l <= r:
            m = (l+r)//2 ## Mid will co-inside with l for n = 2

            ## We will always check and return mid point
            if nums[m] == target:
                return m
            ## Already checked mid point, serach rigth if the target is more
            elif target > nums[m]:
                l = m+1
            else:
                r = m -1
        ## We searched entire range and came here means we could not find.
        return - 1
