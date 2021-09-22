class Solution:
    def reverse(self, x: int) -> int:
        isNegative = False
        islastDigit = False
        reverse = 0   
        if x == 0:
            return 0
        if x < 0:
            x = abs(x)
            isNegative = True
        
        while x > 0:
            last_digit = x%10
            reverse = reverse*10 + last_digit
            x = x//10
        
        if (reverse >= 2**31 -1):
            return 0
        if (reverse <= -2**31):
            return 0
        
        if isNegative==True:
            return reverse-(2*reverse)
        else:
            return reverse
    
            
            
            
            
        