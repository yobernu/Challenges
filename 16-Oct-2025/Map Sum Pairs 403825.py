# Problem: Map Sum Pairs - https://leetcode.com/problems/map-sum-pairs/description/

class TrieNode:
    def __init__(self):
        self.children: Dict[str, TrieNode] = {}
        self.val: int = 0

class MapSum:
    def __init__(self):
        self.root = TrieNode()
        self.key_map: Dict[str, int] = {}

    def insert(self, key: str, val: int) -> None:
        delta = val - self.key_map.get(key, 0)
        self.key_map[key] = val

        current_node = self.root
        for c in key:
            if c not in current_node.children:
                current_node.children[c] = TrieNode()
            current_node = current_node.children[c]
            current_node.val += delta

    def sum(self, prefix: str) -> int:
        current_node = self.root
        for c in prefix:
            if c not in current_node.children:
                return 0
            current_node = current_node.children[c]
            
        return current_node.val