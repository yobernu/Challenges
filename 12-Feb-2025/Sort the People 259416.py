# Problem: Sort the People - https://leetcode.com/problems/sort-the-people/

class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        # for i in range(len(names)):
        #     for j in range(i+1, len(names)):
        #         if heights[j] > heights[i]:
        #             heights[j], heights[i] = heights[i], heights[j]
        #             names[j], names[i] = names[i], names[j]
        # return names
        my_dict = defaultdict()
        sorted_height = heights[:]
        sorted_height = sorted(sorted_height)
        for i in range(len(names)):
            my_dict[heights[i]] = names[i]
        
        ans = []
        for i in reversed(sorted_height):
            ans.append(my_dict[i])
        return ans



