from typing import List

class Solution:
    def assignUmbrella(self, rain: List[int]) -> List[str]:
        n = len(rain)
        alice_count = 0
        bob_count = 0
        ans = []

        for i in range(n):
            alice_needs = (i < n - 1 and rain[i] == 1 and rain[i + 1] == 1)
            bob_needs = (rain[i] == 1)

            if alice_needs and bob_needs:
                if alice_count <= bob_count:
                    ans.append("Alice")
                    alice_count += 1
                else:
                    ans.append("Bob")
                    bob_count += 1
            elif alice_needs:
                ans.append("Alice")
                alice_count += 1
            elif bob_needs:
                ans.append("Bob")
                bob_count += 1
            else:
                ans.append("None")

        return ans
            
        