# Approach 1 
# Time Complexity, Space Complexity?
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        #Getting the key for the counts available
        def get_key(val, my_dict):
            for key, value in my_dict.items():
                 if val == value:
                     return key
        d = {}
        # Counting occurences of a value in a list
        for num in nums:
            if num in d:
                d[num]+=1
            else:
                d[num] = 1
                
        # Storing the counts in a list
        l1 = d.values()
        
        return get_key(max(l1),d)
