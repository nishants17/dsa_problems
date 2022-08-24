# Approach 1: Using dictionary
# Time Complexity: O(nlogn + nk)
# Space Complexity: O(nlogn + nk)
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        d = {}
        # O(n) TS
        for i in nums:
            if i in d:
                d[i]+=1
            else:
                d[i]=1
                
        # Storing frequency of each elements in a descending order
        l = sorted(d.values())[::-1][0:k]
        # Output list
        op = []
        # O(nk) TS
        for i in l:
            for key, value in d.items():
                if value == i:
                    op.append(key)
                    
        # Returning set since for same frequency keys we will have dupes
        return list(set(op))
    
# Approach 2: 
# Time Complexity: O(nlogn) 
# Space Complexity: O(nlogn)
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        d = {}
        for i in nums:
            if i in d:
                d[i]+=1
            else:
                d[i]=1
                
        # Creating a list of nums with highest frequency
        l = sorted(d.keys(), key = lambda val: d[val], reverse = True)[0:k]
        return l 
      
      
