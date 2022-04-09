class Solution:
    def romanToInt(self, s: str) -> int:
        values = dict(zip(['I', 'V', 'X', 'L', 'C', 'D', 'M', 'IV', 'IX', 'XL', 'XC', 'CD', 'CM'], [
                      1, 5, 10, 50, 100, 500, 1000, 4, 9, 40, 90, 400, 900]))


        i = 0
        sum = 0
        while i < len(s):
            if values.get(s[i:i+2]) != None and i < len(s)-1:
                sum += values[s[i:i+2]]
                i += 2
            else:
                sum += values[s[i]]
                i += 1
        return sum        
                
                