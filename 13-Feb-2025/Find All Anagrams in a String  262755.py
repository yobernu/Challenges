# Problem: Find All Anagrams in a String  - https://leetcode.com/problems/find-all-anagrams-in-a-string/

class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        if len(s) < len(p):
            return []
        p_count = Counter(p)
        # for char in p:
        #     p_count[char] += 1
        window_count = defaultdict(int)
        left = 0
        idx = []

        for right in range(len(s)):
            window_count[s[right]] += 1
            if right - left + 1 == len(p):
                if window_count == p_count:
                    idx.append(left)

                window_count[s[left]] -= 1
                if window_count[s[left]] == 0:
                    del window_count[s[left]]
                left += 1

        return idx