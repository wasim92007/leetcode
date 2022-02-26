class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        #### Neetcode solution for memory optimization
        ##https://www.youtube.com/watch?v=bNvIQI2wAjk
        l = len(nums)
        
        ## Algorithm we will compute and store the prefix with a 1 place shift to the right
        ## for i = r will contain prefix for r-1
        result = [1]*l
        for i in range(1,l):
            result[i] = result[i-1]*nums[i-1]
            
        ## Now we will compute the prefix and multiply in position
        postfix = 1 ## Intially the postfix will be 1
        for i in range(l-1, -1,-1):
            ## result already has prefix, we will multiply with postfix
            result[i] = postfix*result[i]
            
            ## Now we will update the postfix
            postfix *= nums[i]
            
        return result
        
        #### My implementation
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
                
