from collections import defaultdict
from typing import List

class Solution:
    def divisibleGame(self, nums: List[int]) -> int:
        MOD = 10**9 + 7
        n = len(nums)

        pref = [0] * (n + 1)
        for i, x in enumerate(nums):
            pref[i + 1] = pref[i] + x

        prime_indices = defaultdict(list)
        for i, x in enumerate(nums):
            temp = x
            d = 2
            while d * d <= temp:
                if temp % d == 0:
                    prime_indices[d].append(i)
                    while temp % d == 0:
                        temp //= d
                    
                    
                
                d += 1
            if temp > 1:
                prime_indices[temp].append(i)

        best_diff = -min(nums)
        best_k = 2

        for p in sorted(prime_indices.keys()):
            idxs = prime_indices[p]
            cur = nums[idxs[0]]
            max_p = cur
            for j in range(1, len(idxs)):
                prev_i = idxs[j - 1]
                curr_i = idxs[j]
                gap_sum = pref[curr_i] - pref[prev_i + 1]
                cur = max(nums[curr_i], cur - gap_sum + nums[curr_i])
                if cur > max_p:
                    max_p = cur

            if max_p > best_diff:
                best_diff = max_p
                best_k = p
        
        return (best_diff * best_k) % MOD
                
            