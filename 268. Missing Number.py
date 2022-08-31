# Approach 1: Using math formula sum(n) = n(n+1) / 2
class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        # Sum of n consecutive numbers
        add = ((len(nums)) * (len(nums)+1)) / 2
        missing_num = add - sum(nums)
        return int(missing_num)

# Approach 2: Using bit manipulations XOR
# [3,0,1]
# op = 2
# Approach 2: Using bit manipulations XOR
class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        num = 0
        for ele in range(1 , len(nums)+1):
            num^= ele
        for ele in nums:
            num^=ele
        return num

        
