class Solution:
    def mySqrt(self, x: int) -> int:
        
        ## Faster solution in the discussion
        
        left, right = 1, x
        while left <= right:
            mid = (left + right) // 2
            pivot = mid * mid
            if pivot == x:
                return mid
            
            if pivot > x:
                right = mid - 1
            else:
                left = mid + 1
        
        return left - 1
        
        
        ## Babylonian Method
        # https://www.youtube.com/watch?v=RQmjgvWbMd8
        
        if x < 1:
            return 0
        else:
            x_n = 0.5 * x
            change = 1
            while change > 0.01:
                next_n = 0.5 * (x_n + x/x_n)
                change = abs(x_n - next_n)
                x_n = next_n
            return (int(x_n))
