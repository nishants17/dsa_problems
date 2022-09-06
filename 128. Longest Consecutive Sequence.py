# Approach 1: Using sorted()
# Complexity: TS O(nlogn)
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        op_l = []
        d = {}
        l = 0
        r = l+1
        nums = sorted(nums)
        ctr = 0
        if len(set(nums)) == 1:
            return 1
        elif len(nums) > 1:
            while r < len(nums):
                if nums[r] - nums[l] == 1:
                    op_l.extend([nums[l],nums[r]])
                    l=r
                    r+=1
                elif nums[r] - nums[l] == 0:
                    l=r
                    r+=1
                elif nums[r] - nums[l] > 1:
                    #op_l.clear()
                    d[ctr] = set(op_l)
                    op_l.clear()
                    ctr+=1
                    l=r
                    r+=1
                d[ctr] = set(op_l)
                print(d)
            return max([1 if len(x)==0 else len(x) for x in d.values()])
        else:
            return 0

# Approach 2: Using Sets
# Complexity: TS O(N)
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        res_Set = set(nums)
        max_length = 0
        for num in nums:
            length = 0
            if (num - 1) not in res_Set:
                while num in res_Set:
                    length+=1
                    num+=1
            max_length = max(max_length, length)
        return max_length
