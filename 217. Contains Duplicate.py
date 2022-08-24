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
# Time Complexity: O(n)
# Space Complexity: O(n)
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        return not len(set(nums)) == len(nums)

# Approach 3: Using sort and iteration
# Time Complexity: O(n)
# Space Complexity: O(n)
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        nums.sort()
        i = 0
        while i < len(nums):
            if i+1 < len(nums) and nums[i] == nums[i+1]:
                return True
            else:
                i+=1
        return False
