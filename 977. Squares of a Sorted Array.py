# Approach 1: Return sorted squares from the input array
class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        return sorted([i*i for i in nums])
      
# Approach 2: Two Pointers Approach (Using deque and w/o deque)
