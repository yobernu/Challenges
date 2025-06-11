# Problem: Bitwise XOR of All Pairings - https://leetcode.com/problems/bitwise-xor-of-all-pairings/description/?envType=problem-list-v2&envId=brainteaser

class Solution:
    def xorAllNums(self, nums1: List[int], nums2: List[int]) -> int:
        first = nums1[0]
        for i in range(1, len(nums1)):
            first ^= nums1[i]
        
        second = nums2[0]
        for i in range(1, len(nums2)):
            second ^= nums2[i]
        
        result, n, m = 0, len(nums1), len(nums2)
        if n % 2 == 1:
            result ^= second
        if m % 2 == 1:
            result ^= first
        return result    

        
