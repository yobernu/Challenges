# Problem: Count Number of Distinct Integers After Reverse Operations - https://leetcode.com/problems/count-number-of-distinct-integers-after-reverse-operations/

class Solution:
    def countDistinctIntegers(self, nums: List[int]) -> int:
        ans = [i for i in nums]
        for num in nums:
            rev = str(num)[::-1]
            ans.append(int(rev))
        counter = Counter(ans)
        return len(counter)


    """
    [10,12,31]



    """