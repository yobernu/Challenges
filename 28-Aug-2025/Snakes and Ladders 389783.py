# Problem: Snakes and Ladders - https://leetcode.com/problems/snakes-and-ladders/

class Solution:
    def snakesAndLadders(self, board: List[List[int]]) -> int:
        n = len(board)
        
        def get_coordinates(s):
            row = n - 1 - (s - 1) // n
            col = (s - 1) % n
            if (n - row) % 2 == 0:
                col = n - 1 - col
            return row, col

        visited = set()
        q = deque()
        q.append((1, 0))
        while q:
            s, moves = q.popleft()
            for i in range(1, 7):
                nxt = s + i
                if nxt > n * n:
                    continue
                r, c = get_coordinates(nxt)
                if board[r][c] != -1:
                    nxt = board[r][c]
                if nxt == n * n:
                    return moves + 1
                if nxt not in visited:
                    visited.add(nxt)
                    q.append((nxt, moves + 1))
        return -1