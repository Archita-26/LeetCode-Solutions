class Solution:
    def minRange(self, a: int, b: int, c: int) -> int:
        x, y, z = sorted([a, b, c])
        return min(z - x, y)