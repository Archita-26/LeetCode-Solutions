class Solution:
    def minSumSquareDiff(
        self, nums1: list[int], nums2: list[int], k1: int, k2: int) -> int:
        diff = [abs(a - b) for a, b in zip(nums1, nums2)]
        total_k = k1+ k2

        if sum(diff) <= total_k:
            return 0
        
        max_val = max(diff)
        count = [0] * (max_val + 1)
        for d in diff:
            count[d] += 1

        for v in range(max_val, 0, -1):
            if count[v] > 0:
                if total_k >= count[v]:
                    total_k -= count[v]
                    count[v - 1] += count[v]
                    count[v] = 0
                else:
                    count[v - 1] += total_k
                    count[v] -= total_k
                    break
        return sum(c * (v * v) for v, c in enumerate (count))
        