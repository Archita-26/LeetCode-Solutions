from typing import List

class Solution:
    def getSum(self, nums: List[int]) -> int:
        n = len(nums)
        pref = [0] * (n+1)
        for i, x in enumerate(nums):
            pref[i + 1] = pref[i] + x

        #Iterative Segment Tree for Range Maximum Query on pref
        size = 1
        while size < n + 1:
            size <<= 1
        INF = 10**18
        tree = [-INF] * (2 * size)
        for i, v in enumerate(pref):
            tree[size + i] = v
        for i in range(size - 1, 0, -1):
            tree[i] = tree[2 * i] if tree[2 * i] > tree[2 * i + 1] else tree[2 * i + 1]

        def rmq(l: int, r: int) -> int:
            res = -INF
            l += size
            r += size
            while l <= r:
                if l & l:
                    if tree[l] > res:
                       res = tree[l]
                    l += 1
                if not (r & 1):
                    if tree[r] > res:
                       res = tree[r]
                    r -= 1
                l >>= 1
                r >>= 1
            return res
    
    #Manacher's Algorithm
        t = [None] * (2 * n + 1)
        for i, x in enumerate(nums):
            t[2 * i + 1] = x

        m = len(t)
        p = [0] * m
        center = right = 0
        for i in range(m):
            if i < right:     
                p[i] = min(right - i, p[2 * center - i])
            while i - p[i] - 1 >= 0 and i + p[i] + 1 < m and t[i - p[i] - 1] == t[i + p[i] + 1]:
                p[i] += 1
            if i + p[i] > right:
                center = i
                right = i + p[i]

        ans = -INF
    #Odd-length palindromes
        for i in range(n):
            r = p[2 * i + 1] // 2
            max_pref = rmq(i + 1, i + r + 1)
            val = nums[i] + 2 * (max_pref - pref[i + 1])
            if val > ans:
                ans = val

    #Even-length palindromes
        for i in range(n - 1):
            r = p[2 * i + 2] // 2
            if r > 0:
                max_pref = rmq(i + 2, i + r + 1)
                val = 2 * (max_pref - pref[i + 1])
                if val > ans:
                    ans = val 

        return ans