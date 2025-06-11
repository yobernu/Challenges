# Problem: Letter Case Permutation - https://leetcode.com/problems/letter-case-permutation/

class Solution:
    def letterCasePermutation(self, s: str) -> List[str]:
        letter_indices = [i for i, c in enumerate(s) if c.isalpha()]
        result = []
        n = len(letter_indices)

        for mask in range(1 << n):
            chars = list(s)
            for j in range(n):
                idx = letter_indices[j]
                if (mask >> j) & 1:
                    chars[idx] = chars[idx].upper()
                else:
                    chars[idx] = chars[idx].lower()
            result.append("".join(chars))
        
        return result
