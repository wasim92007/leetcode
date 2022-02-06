class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        ## Algorithm::=
        ## We will create two accumulative product arrayL l2r and r2l.
        ## For i^th element we will multiply l2r[i-1] with r2l[i+1]
        
        l = len(nums)
        
        ## We will construct a Right to Left Accumulated product list
        r2l_prod_arr = [0]*l
        for i in range(len(nums)-1, -1, -1):
            if i == len(nums)-1 :
                r2l_prod_arr[i] = nums[i]
                #print('i, nums[i], r2l_prod_arr', i, nums[i], r2l_prod_arr)
            else:
                r2l_prod_arr[i] = r2l_prod_arr[i+1] * nums[i]
                #print('i, nums[i], r2l_prod_arr', i, nums[i], r2l_prod_arr)
                
                
        ## We will construct a Left to Right Accumulated product list
        l2r_prod_arr = [0]*l
        result = [0]*l
        for i in range(0, l):
            if i == 0:
                l2r_prod_arr[i] = nums[i]
                result[i]       = r2l_prod_arr[(i+1)]
                #print('i, nums[i], l2l_prod_arr, result', i, nums[i], l2r_prod_arr, result)
            else:
                l2r_prod_arr[i] = l2r_prod_arr[i-1] * nums[i]
                if i == l - 1:
                    result[i]       = l2r_prod_arr[i-1]
                    #print('i, nums[i], l2l_prod_arr, result', i, nums[i], l2r_prod_arr, result)
                else:
                    result[i]       = l2r_prod_arr[i-1]*r2l_prod_arr[i+1]
                    #print('i, nums[i], l2l_prod_arr, result', i, nums[i], l2r_prod_arr, result)
                    
        return result
