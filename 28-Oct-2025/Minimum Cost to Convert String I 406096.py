# Problem: Minimum Cost to Convert String I - https://leetcode.com/problems/minimum-cost-to-convert-string-i/description/?envType=problem-list-v2&envId=shortest-path

class Solution:
    def minimumCost(self, source: str, target: str, original: List[str], changed: List[str], cost: List[int]) -> int:

        totalCost = 0
        dist = [[float("inf")]*26 for _ in range(26)]
        
        for org, chg, cst in zip(original, changed, cost):
            startIdx = ord(org) - ord("a")
            endIdx = ord(chg) - ord("a")
            dist[startIdx][endIdx] = min(dist[startIdx][endIdx] , cst)


        for i in range(26):
            dist[i][i] = 0


        for k in range(26):
            for i in range(26):
                for j in range(26):
                    dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])

        for src, tgt in zip(source, target):
            if src == tgt:
                continue
            source_char = ord(src) - ord("a")
            target_char = ord(tgt) - ord("a")

            if dist[source_char][target_char] == float("inf"):
                return -1
            totalCost += dist[source_char][target_char]
        return totalCost
