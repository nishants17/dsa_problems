# Approach 1: Using dictionary
# Time Complexity: O(N) or O(N**2)
# Space Complexity: O(N)
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        d = {}
        for i in nums:
            if i in d:
                d[i]+=1
            else:
                d[i]=1
                
        # Storing frequency of each elements in a descending order
        l = sorted(d.values())[::-1][0:k]
        # Output list
        op = []
        for i in l:
            for key, value in d.items():
                if value == i:
                    op.append(key)
                    
        # Returning set since for same frequency keys we will have dupes
        return list(set(op))
      
      
