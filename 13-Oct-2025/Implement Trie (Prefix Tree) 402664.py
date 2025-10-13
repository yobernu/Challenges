# Problem: Implement Trie (Prefix Tree) - https://leetcode.com/problems/implement-trie-prefix-tree/

class Node:
    def __init__(self):
        self.children = [None for _ in range(26)]
        self.is_end = False
class Trie:
    def __init__(self):
        self.root = Node()

    def insert(self, word: str) -> None:
        current_node = self.root
        for c in word:
            idx = ord(c) - ord("a")
            if not current_node.children[idx]:
                current_node.children[idx] = Node()
            current_node = current_node.children[idx]
        current_node.is_end = True

    def search(self, word: str) -> bool:
        current_node = self.root
        for c in word:
            idx = ord(c) - ord("a")
            if not current_node.children[idx]:
                return False
            current_node = current_node.children[idx]
        return current_node.is_end
        

    def startsWith(self, prefix: str) -> bool:
        current_node = self.root
        for c in prefix:
            idx = ord(c) - ord("a")
            if not current_node.children[idx]:
                return False
            current_node = current_node.children[idx]
        return True
        


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)