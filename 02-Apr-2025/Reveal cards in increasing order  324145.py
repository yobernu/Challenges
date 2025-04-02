# Problem: Reveal cards in increasing order  - https://leetcode.com/problems/reveal-cards-in-increasing-order/

class Solution:
    def deckRevealedIncreasing(self, deck: List[int]) -> List[int]:
        deck.sort()
        q = deque([i for i in range(len(deck))])
        f = []
        for i in range(len(deck)):
            if q:
                f.append(q.popleft())
                if q:
                    q.append(q.popleft())
                
        ans = [0]*len(deck)
        for d, i in zip(deck, f):
            ans[i] = d
        # print(f)
        return ans

