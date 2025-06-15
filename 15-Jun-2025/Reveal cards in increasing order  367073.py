# Problem: Reveal cards in increasing order  - https://leetcode.com/problems/reveal-cards-in-increasing-order/

class Solution:
    def deckRevealedIncreasing(self, deck: List[int]) -> List[int]:
        n = len(deck)
        newArr = [0] * n
        sor = deque(sorted(deck))
        jump = False
        while sor:
            for i in range(n):
                if newArr[i] == 0:
                    if not jump:
                        newArr[i] = sor[0]
                        sor.popleft()
                    jump = not jump
        return newArr
