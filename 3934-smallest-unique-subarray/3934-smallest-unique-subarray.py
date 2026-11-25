from typing import List

class Solution:
    def smallestUniqueSubarray(self, nums: List[int]) -> int:
        n = len(nums)
        size = 2 * n + 1
        nxt = [{} for _ in range(size)]
        link = [-1] * size
        length = [0] * size
        cnt = [0] * size
        last = 0
        sz = 1

        for x in nums:
            cur = sz
            sz += 1
            length[cur] = length[last] + 1
            cnt[cur] = 1
            p = last
            while p != -1 and x not in nxt[p]:
                nxt[p][x] = cur
                p = link[p]
            if p == -1:
                link[cur] = 0
            else:
                q = nxt[p][x]
                if length[p] + 1 == length[q]:
                    link[cur] = q
                else:
                    clone = sz
                    sz += 1
                    length[clone] = length[p] + 1
                    nxt[clone] = nxt[q].copy()
                    link[clone] = link[q]
                    while p != -1 and nxt[p].get(x) == q:
                        nxt[p][x] = clone
                        p = link[p]
                    link[q] = link[cur] = clone
            last= cur

        order = sorted(range(sz), key=length.__getitem__, reverse=True)
        for v in order:
            if link[v] != -1:
                cnt[link[v]] += cnt[v]

        ans = n
        for v in range(1, sz):
            if cnt[v] == 1:
                cand = length[link[v]] + 1
                if cand < ans:
                    ans = cand
                
        return ans
