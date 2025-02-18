# Problem: Subarray Sums Divisible by K - https://leetcode.com/problems/subarray-sums-divisible-by-k/

class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        hash_map = defaultdict(int)
        hash_map[0] = 1  
        temp = 0
        ans = 0
        for num in nums:
            temp += num
            remainder = temp % k
            if remainder < 0:
                remainder += k  
            ans += hash_map[remainder]
            hash_map[remainder] += 1
        
        return ans




    