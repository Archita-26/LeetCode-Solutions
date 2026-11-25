from typing import List

class Solution:
    def maxDigitRange(self, nums: List[int]) -> int:
        max_range = -1
        total = 0

        for num in nums:
            digits = str(num)
            digit_range = int(max(digits)) - int(min(digits))
            if digit_range > max_range:
                max_range = digit_range
                total = num
            elif digit_range == max_range:
                total += num
            
        return total