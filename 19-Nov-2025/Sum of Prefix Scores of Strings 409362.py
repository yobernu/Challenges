# Problem: Sum of Prefix Scores of Strings - https://leetcode.com/problems/sum-of-prefix-scores-of-strings/description/

class TrieNode:
    def __init__(self):
        self.is_end=False
        self.children=[None for _ in range(26)]
        self.count=0
class Trie:
    def __init__(self):
        self.root=TrieNode()
    def insert(self,word):
        cur=self.root
        for char in word:
            idx=ord(char)-97
            if cur.children[idx] is None:
                cur.children[idx]=TrieNode()
            cur=cur.children[idx]
            cur.count+=1
    def get_score(self,word):
        score=0
        cur=self.root
        for char in word:
            idx=ord(char)-97
            if cur.children[idx] is not None:
                cur=cur.children[idx]
                score+= cur.count
        return score



class Solution:
    def sumPrefixScores(self, words: List[str]) -> List[int]:
        result=[]
        trieNode=Trie()

        for word in words:
            trieNode.insert(word)
        for word in words:
            score=trieNode.get_score(word)
            result.append(score)
        return result

        