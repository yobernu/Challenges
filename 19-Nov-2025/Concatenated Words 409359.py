# Problem: Concatenated Words - https://leetcode.com/problems/concatenated-words/

def solve(word: str, s: set, memo: dict) -> bool:
    if word in memo:
        return memo[word]
    
    for i in range(1, len(word)):
        left, right = word[:i], word[i:]
        if left in s:
            if right in s or solve(right, s, memo):
                memo[word] = True
                return True
    
    memo[word] = False
    return False

class Solution:
    def findAllConcatenatedWordsInADict(self, words: List[str]) -> List[str]:
        s = set(words)
        ans = []
        memo = {}
        
        for word in words:
            if solve(word, s - {word}, memo):
                
                ans.append(word)
        
        return ans