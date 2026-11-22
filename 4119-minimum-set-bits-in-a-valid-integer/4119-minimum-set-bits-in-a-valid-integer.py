from typing import List

class Solution:
    def minSetBits(self, nums: List[int], k: int) -> int:
        n = len(nums)
        pref = [0] * n
        suff = [0] * n

        for i in range(n):
            if i % k == 0:
                pref[i] = nums[i]
            else:
                pref[i] = pref[i - 1] & nums[i]

        for i in range(n - 1, -1, -1):
            if i == n - 1 or (i + 1) % k == 0:
                suff[i] = nums[i]
            else:
                suff[i] = suff[i + 1] & nums[i]

        xs = set()
        max_val = 0
        for i in range(n - k + 1):
            x = suff[i] & pref[i + k - 1]
            if x == 0:
                return -1
            xs.add(x)
            if x > max_val:
                max_val = x

        B = max_val.bit_length()
        size = 1 << B
        bad = bytearray(size)
        for x in xs:
            bad[x] = 1

        for b in range(B):
            bit = 1 << b 
            for mask in range(bit, size, bit << 1):
                for m in range(mask, mask + bit):
                    if bad[m ^ bit]:
                        bad[m] = 1

        max_pop = 0
        for m in range(size):
            if not bad[m]:
                pc = m.bit_count()
                if pc > max_pop:
                    max_pop = pc

        return B - max_pop