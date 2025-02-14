# Problem: 3Sum - https://leetcode.com/problems/3sum/description/

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
            nums.sort()
            ans = set()
            for left in range(len(nums)-2):
                right = left + 1
                end = len(nums)-1
                while right < end:
                    if nums[left] + nums[right] + nums[end] < 0 :
                        right += 1
                    elif nums[left] + nums[right] + nums[end] > 0:
                        end -= 1
                    else:
                        ans.add((nums[left], nums[right], nums[end]))
                        right+=1
                        end -= 1
                    
            return list(map(list, ans)) 


                