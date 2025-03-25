# Problem: N-Queens - https://leetcode.com/problems/n-queens/description/

class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        col = set()
        diag = set()
        a_diag = set()
        ans = [["."] * n for _ in range(n)]
        final_boss = []
        def helper(r):
            if  r == n:
                new_boss = []
                for row in ans:
                    new_boss.append("".join(row))
                final_boss.append(new_boss)
                return

            for c in range(n):
                if c  in col or r-c  in diag or r+c in a_diag:
                    continue
                else:
                    col.add(c)
                    diag.add(r-c)
                    a_diag.add(r+c)
                    ans[r][c] = "Q"
                    helper(r+1)
                    ans[r][c] = "."
                    col.remove(c)
                    diag.remove(r - c)
                    a_diag.remove(r + c)

        helper(0)
        return final_boss
        

               
            
        