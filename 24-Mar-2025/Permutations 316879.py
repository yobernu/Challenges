# Problem: Permutations - https://leetcode.com/problems/permutations/

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        answer = []
        k=len(nums)
        path = []

        def helper():
            if len(path) ==k:
                answer.append(path[:])
                return
            for num in nums:
                if num in path:
                    continue
                path.append(num)
                helper()
                path.pop()
        helper()
        return answer