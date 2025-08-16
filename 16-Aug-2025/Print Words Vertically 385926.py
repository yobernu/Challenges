# Problem: Print Words Vertically - https://leetcode.com/problems/print-words-vertically/description/

class Solution:
    def printVertically(self, s: str) -> List[str]:
        words = s.split()
        max_length = 0
        length = 1
        idx = 0
        temp = ""
        max_length = len(words)
        length = 0
         
        for i in words:
            length = max(length, len(i))
        ans = ['' for _ in range(length)]
        
        i = 0
        for word in words:
            for char in word:
                ans[i] += char
                i+=1
            while i < length:
                ans[i] += " "
                i+=1
            i = 0
        cleaned_words = [word.rstrip() for word in ans]
        return cleaned_words

