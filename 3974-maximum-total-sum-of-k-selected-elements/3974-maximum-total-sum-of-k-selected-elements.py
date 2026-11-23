from typing import List

class Solution:
    def maxSum(self, nums: List[int], k: int, mul: int) -> int:
        nums.sort(reverse=True)
        total = 0
        for i in range(k):
            total += nums[i] * max(1, mul - i)
        return total