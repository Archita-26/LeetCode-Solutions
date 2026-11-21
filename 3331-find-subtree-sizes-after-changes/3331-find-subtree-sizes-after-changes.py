import sys
from typing import List

sys.setrecursionlimit(200000)

class Solution:
    def findSubtreeSizes(self, parent: List[int], s: str) -> List[int]:
        n = len(parent)
        adj = [[] for _ in range(n)]
        for i in range(1, n):
            adj[parent[i]].append(i)

        new_parent = list(parent)
        last_seen = [-1] * 26

        def dfs_reparent(u: int) -> None:
            c = ord(s[u]) - ord('a')
            prev = last_seen[c]
            if prev != -1:
                new_parent[u] = prev
            last_seen[c] = u
            for v in adj[u]:
                dfs_reparent(v)
            last_seen[c] = prev

        dfs_reparent(0)

        new_adj = [[] for _ in range(n)]
        for i in range(1, n):
            new_adj[new_parent[i]].append(i)

        ans = [1] * n

        def dfs_size(u: int) -> int:
            for v in new_adj[u]:
                ans[u] += dfs_size(v)
            return ans[u]

        dfs_size(0)
        return ans
        