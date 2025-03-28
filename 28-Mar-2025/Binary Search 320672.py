# Problem: Binary Search - https://leetcode.com/problems/binary-search/description/

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums)
        def recurse(left, right):
            mid = (left+right)//2
            if left > right:
                return -1
            if nums[mid] == target:
                return mid
            else:
                if nums[mid] < target:
                    return recurse(mid+1, right)
                else:
                    return recurse(left, mid-1)
        return recurse(0, len(nums)-1)



        # while left <= right:
        #     mid = (left + right)//2
        #     if target > nums[mid]:
        #         left = mid + 1
        #     elif target < nums[mid]:
        #         right = mid - 1
        #     elif left > right:
        #         return -1
        #     else:
        #         break
            
        # return mid