class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = 0
        r = l+1
        d = {}
        ctr = 0
        for i in range(0,len(s)):
            if s[l] != s[r] and r < len(s):
                if d:
                    if s[l] in d[ctr]:
                        l = r
                        break
                    d[ctr].append(s[l])
                else:
                    d[ctr] = list(s[l])
        print(d)
        return [k for k in d.keys() if len(d.get(k))==max([len(n) for n in d.values()])]


# Approach using a set
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        charSet = set()
        l = 0
        res = 0
        for r in range(len(s)):
            while s[r] in charSet:
                charSet.remove(s[l])
                l+=1
            charSet.add(s[r])
            res = max(res, r - l + 1)
        return res

        
