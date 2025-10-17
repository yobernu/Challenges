# Problem: Replace Words - https://leetcode.com/problems/replace-words/

class Node:
    def __init__(self):
        self.dictionary = [None for _ in range(26)]
        self.isWord = False

class Solution:
    def replaceWords(self, dictionary: List[str], sentence: str) -> str:
        self.root = Node()
        sentence_list = sentence.split()
        for root in dictionary:
            self.insert(root)   
        sentence_list = sentence.split()
        replaced = [self.search(word) for word in sentence_list]
        return ' '.join(replaced)



    def search(self, word):
        current_node = self.root
        carry = '' 
        for c in word:
            idx = ord(c) - ord('a')
            if not current_node.dictionary[idx]:
                return word
            carry += c
            current_node = current_node.dictionary[idx]
            if current_node.isWord:
                return carry
        return word
        

    def insert(self, word):
        current_node = self.root
        for c in word:
            idx = ord(c) - ord('a')
            if not current_node.dictionary[idx]:
                current_node.dictionary[idx] = Node()
            current_node = current_node.dictionary[idx]
        current_node.isWord = True
    

        
