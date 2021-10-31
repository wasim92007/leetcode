class Solution:
    def countAndSay(self, n: int) -> str:
        
        ## Let us bypath the base code for faster execution
        if n == 1:
            return '1'
        
        ## Declare an dp array
        dp = ['1']*n
        
        ## As we have base case filled, we will start with n=2
        ## We are using a 0 based indexing here, we will fill
        ## the dp array till n-1
        for i in range(1,n):
            ## Let us get a place holder for say
            word = ''
            ## Let's get the number of elements in the last word
            l = len(dp[i-1])
            ## Let us initialize the last char with first char
            last_char = dp[i-1][0]
            ## Let us use a iteration variable j and count both
            ## initialized to 0
            j, count = 0, 0
            ## We will traverse through the last say once
            while l - j > 0:
                ## We will write the last count and char if there is a mismatch
                ## We need to update the last_char with current char
                ## We also need to reset the count to 1 as we used the current
                ## char for checking
                ## finally we need to update the loop variable
                if dp[i-1][j] != last_char:
                    word+= str(count)+last_char; last_char = dp[i-1][j]; count=1; j+= 1
                else:
                    ## We will increament count and loop variable if there is a
                    ## match
                    j+= 1; count+=1
                    
            ## We need to write back the last count as the while loop will not 
            ## write for the last count
            word+=str(count)+last_char
            
            ## Add back the word to the dp array
            dp[i] = word
        
        ## Return the result, again we used a 0 based system
        return dp[n-1]
