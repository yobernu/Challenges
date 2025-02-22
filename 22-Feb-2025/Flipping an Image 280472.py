# Problem: Flipping an Image - https://leetcode.com/problems/flipping-an-image/description/

class Solution:
    def flipAndInvertImage(self, image: List[List[int]]) -> List[List[int]]:
        flipped = [lst[::-1] for lst in image]
        ans = []
        for i in flipped:
            temp = []
            for j in i:
                if j == 0:
                    temp.append(1)
                else:
                    temp.append(0)
            ans.append(temp)
        return ans
