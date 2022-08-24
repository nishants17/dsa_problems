# Approach 1: Hash map
# Time Complexity: O(n)
# Space Complexity: O(n)
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        counter = {}
        for i in nums:
            counter[i] = 1 + counter.get(i, 0)
            if counter[i] > 1:
                return True
        return False
      
# Approach 2: Using a set
# Time Complexity: 
# Space Complexity: 
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        return not len(set(nums)) == len(nums)
