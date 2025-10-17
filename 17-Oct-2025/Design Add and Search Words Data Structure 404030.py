# Problem: Design Add and Search Words Data Structure - https://leetcode.com/problems/design-add-and-search-words-data-structure/

class Node:
    def __init__(self):
        self.dictionary = [None for _ in range(26)]
        self.isWord = False
class WordDictionary:

    def __init__(self):
        self.root = Node()
    
    def addWord(self, word: str) -> None:
        current_node = self.root
        for c in word:
            idx = ord(c) - ord("a")
            if not current_node.dictionary[idx]:
                current_node.dictionary[idx] = Node()
            current_node = current_node.dictionary[idx]
        current_node.isWord = True


    # def search(self, word: str) -> bool:
    #     def dfs(node, idx):
    #         if idx == len(word):
    #             return node.isWord
    #         elif node.dictionary[idx] == ".":
    #             for child in node.dictionary:
    #                 if child and dfs(child, idx+1):
    #                     return True
    #                 return False
    #         else:
    #             idx_char = ord('a') - ord(word[idx])
    #             if not node.dictionary[idx_char]:
    #                 return False
    #             return dfs(node.dictionary[idx_char], idx + 1)
    #     return dfs(self.root, 0)







    def search(self, word: str) -> bool:
        def dfs(node, idx):
            if idx == len(word):
                return node.isWord
            if word[idx] == '.':
                for child in node.dictionary:
                    if child and dfs(child, idx + 1):
                        return True
                return False
            else:
                idx_char = ord(word[idx]) - ord('a')
                if not node.dictionary[idx_char]:
                    return False
                return dfs(node.dictionary[idx_char], idx + 1)
        
        return dfs(self.root, 0)

        


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)