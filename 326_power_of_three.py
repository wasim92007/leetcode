class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        
        ## Better solution:
        ## https://www.youtube.com/watch?v=M2P2BAFmLlo
        ## Exploits the fact the for n < 2^31 -1
        ## 3^19 is the max possible within the range
        ## Hence, any power of 3 within this range should
        ## divide the 3^19
        
        x = 3**19
        
        ## Remember we have to use n > 0, as we are using division in modulo
        return n>0 and x%n == 0

        
        ## My method: Here n does not follow the given constraint
        ## or n is >= 0, as compared to the constraint given
        x, i = 1, 0
        while n >= x:
            if x == n:
                return True
            else:
                i += 1
                x = 3**i
                
        return False
            
        
        
