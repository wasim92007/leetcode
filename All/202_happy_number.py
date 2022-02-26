class Solution:
    def isHappy(self, n: int) -> bool:
        
        def sum_digit_squares(n):
            sum = 0
            while n:
                sum += (n%10)**2
                n = n//10
            return sum
        
        sods_set = set()
        
        while True:
            n = sum_digit_squares(n)
            if n == 1:
                return True
            else:
                if n in sods_set:
                    return False
                else:
                    sods_set.add(n)
        
