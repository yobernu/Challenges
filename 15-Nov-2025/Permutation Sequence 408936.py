# Problem: Permutation Sequence - https://leetcode.com/problems/permutation-sequence/description/

class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        self.count = 0
        self.result = None

        def backtrack(path, used):
            if len(path) == n:
                self.count += 1
                if self.count == k:
                    self.result = ''.join(map(str, path))
                return

            for i in range(1, n+1):
                if used[i]:
                    continue
                used[i] = True
                path.append(i)
                backtrack(path, used)
                path.pop()
                used[i] = False
                if self.result:
                    return

        used = [False] * (n+1)
        backtrack([], used)
        return self.result