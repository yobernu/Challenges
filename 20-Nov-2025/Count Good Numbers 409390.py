# Problem: Count Good Numbers - https://leetcode.com/problems/count-good-numbers/

class Solution:
    def countGoodNumbers(self, n: int) -> int:
        mod = 10**9 + 7
        def pow(x,n):
            # if n==1:
            #     return x

            if n==0:
                return 1
            if n%2 == 0:
                y = pow(x,n//2)%mod
                return y*y

            if n%2 == 1:
                return x*pow(x,n-1)%mod


        if n%2 == 0:
            odd = even = n//2

        else:
            odd = (n-1)//2
            even = n-((n-1)//2)

        
        return (pow(4,odd) * pow(5,even))%(10**9 + 7)

