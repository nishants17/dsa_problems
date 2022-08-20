# Time Complexity : 0(1)
# Space Complexity : 0(1)
class Solution:
    def romanToInt(self, s: str) -> int:
        d = {'I':1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000}
        sum = 0
        i = 0
        while i < len(s):
            if i+1 < len(s) and d[s[i]] < d[s[i+1]]:
                sum+= d[s[i+1]] - d[s[i]]
                i = i+2
            else:
                sum+=d[s[i]]
                i = i+1
        return sum

# Think of alternative approaches
