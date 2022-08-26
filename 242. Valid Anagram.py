# Approach 1: Using Sorted
# Time Complexity: O(nlogn)
# Space Complexity: O(nlogn)
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if sorted(s) == sorted(t):
            return True
        else:
            return False
        
# Approach 2: Using Hash Maps
# Time Complexity: O(N+M)
# Space Complexity: O(N+M)
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        d = {}
        # Counting string occurences in s 
        for ele in s:
            if ele in d:
                d[ele]+=1
            else:
                d[ele] = 1
        d1 = {}
        # Counting string occurences in t
        for ele in t:
            if ele in d1:
                d1[ele]+=1
            else:
                d1[ele] = 1
        return d == d1
    
# Approach 3: Using Hash Maps with get
# Time Complexity: O(N+M)
# Space Complexity: O(N+M)
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        d = {}
        # Counting string occurences in s 
        for ele in s:
            d[ele] = 1 + d.get(ele, 0)
        d1 = {}
        # Counting string occurences in t
        for ele in t:
            d1[ele] = 1 + d1.get(ele, 0)
        return d == d1
