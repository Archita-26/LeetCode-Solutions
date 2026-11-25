class Solution:
    def canMakeSubsequence(self, s: str, t: str) -> bool:
        n, m = len(s), len(t)
        if n > m:
            return False

        pref = [m] * (n + 1)
        pref[0] = - 1
        p = 0
        for i in range(n):
            while p < m and t[p] != s[i]:
                p += 1
            if p < m:
                pref[i + 1] = p
                p += 1
            else:
                break
        
        if pref[n] < m:
            return True

        suff = [-1] * (n + 1)
        suff[n] = m
        p = m - 1
        for i in range( n - 1, - 1, -1):
            while p >= 0 and t[p] != s[i]:
                p -= 1
            if p >= 0:
                suff[i] = p
                p -= 1
            else:
                break
            
        for i in range(n):
            if pref[i] < m and suff[i + 1] >= 0 and pref[i] + 1 < suff[i + 1]:
                return True
                
        return False