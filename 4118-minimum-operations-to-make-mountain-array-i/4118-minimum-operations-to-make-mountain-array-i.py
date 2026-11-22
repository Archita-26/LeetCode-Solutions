from itertools import accumulate
from typing import List

class Solution:
     def minOperations(self, nums: List[int]) -> int:
         n = len(nums)
         if n < 3:
             return -1

         M = max(nums)

         g = [None] * n
         g_prev = [0] * M
         for i in range(n - 1):
            y = nums[i] - i
            cur =[val + abs(x -y) for x, val in enumerate(g_prev, 1)]
            g_prev = list(accumulate(cur, min))
            g[i] = g_prev

         h = [None] * n
         h_prev = [0] * M
         for i in range(n - 1, 0, -1):
            y = nums[i] - (n - 1 - i)
            cur = [val + abs(x - y) for x, val in enumerate(h_prev, 1)]
            h_prev = list(accumulate(cur, min))
            h[i] = h_prev

         ans = float('inf')
         for p in range(1, n - 1):
            gl = g[p - 1]
            hr = h[p + 1]
            r_dist = n - 1 - p
            target = nums[p]

            lo = max(p + 1, n - p)
            hi = M + max(p, r_dist)

            def cost(v:int) -> int:
                xl = v - p
                xr = v - r_dist
                return gl[(xl if xl < M else M) - 1] + hr[(xr if xr < M else M) - 1] + abs(v - target)

            while lo < hi:
                mid = (lo + hi) // 2
                if cost(mid) <= cost(mid + 1):
                    hi = mid
                else:
                    lo = mid + 1

            c = cost(lo)
            if c < ans:
                ans = c                
         return ans


