# Problem: Shifting Letters II - https://leetcode.com/problems/shifting-letters-ii/description/

class Solution:
    def shiftingLetters(self, s: str, shifts: List[List[int]]) -> str:
        n = len(s)
        new_arr = [0]*(n+1)
        for left, right, direction in shifts:
            if direction == 1:
                new_arr[left] += 1
                new_arr[right + 1] -= 1
            else:
                new_arr[left] -= 1
                new_arr[right + 1] += 1
        for i in range(1, n+1):
            new_arr[i] += new_arr[i-1]

        ans = ""
        arr = [chr(97+i) for i in range(26)]
        for i in range(n):
            letter = ord(s[i]) - 97
            shift = new_arr[i]
            shifted = (letter + shift)%26
            ans += arr[shifted]
        return ans