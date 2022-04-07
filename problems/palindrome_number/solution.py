class Solution:
    def isPalindrome(self, x: int) -> bool:
        a = abs(x)
        b = 0
        while(a):
            b = 10*b +a%10
            a //= 10
        if x==b:
        	return True
        else:
            return False
        