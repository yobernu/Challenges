# Problem: Generate Binary Strings Without Adjacent Zeros - https://leetcode.com/problems/generate-binary-strings-without-adjacent-zeros/description/

class Solution:
    def validStrings(self, n: int) -> List[str]:
        result = []
        def backtrack(s, zero, one):
            if len(s) == n:
                print(s)
                for i in range(n-1):
                    if int(s[i]) + int(s[i+1]) == 0:
                        return
                else:
                    result.append(s)
                    return
            if zero < n:
                backtrack(s + "0", zero + 1, one)
            if one < n:
                backtrack(s + "1", zero, one + 1)
        backtrack("", 0, 0)
        return result
