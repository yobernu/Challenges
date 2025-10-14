# Problem: Longest Word in Dictionary - https://leetcode.com/problems/longest-word-in-dictionary/

class Node:
    def __init__(self):
        self.children = [None for _ in range(26)]
        self.is_end = False
class Solution:
    def __init__(self):
        self.root = Node()
    def longestWord(self, words: List[str]) -> str:
        current_node = self.root
        for word in words:
            self.insert(word, current_node)
        valid_words = set()
        for word in words:
            node = self.root
            valid = True
            for c in word:
                idx = ord(c) - ord("a")
                node = node.children[idx]
                if not node or not node.is_end:
                    valid = False
                    break
            if valid:
                valid_words.add(word)
        return min(valid_words, key=lambda x: (-len(x), x)) if valid_words else ""

        
    def insert(self, word: str, current_node) -> None:
        # current_node = self.root
        for c in word:
            idx = ord(c) - ord("a")
            if not current_node.children[idx]:
                current_node.children[idx] = Node()
            current_node = current_node.children[idx]
        current_node.is_end = True
    