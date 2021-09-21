# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.
from typing import List

class Solution:
    def largestRectangleArea_old(self,heights:List[int])->int:
        max_area=0
        for i in range(len(heights)-1):
            for j in range(i,len(heights)):
                cur_area=min(heights[i:j+1])*(j-i+1)
                max_area=max(max_area,cur_area)
        return max(max_area,max(heights))
    def largestRectangleArea_med(self,heights:List[int])->int:
        if len(heights)==1:
            return heights[0]
        sorted_heights=list(set(heights))
        sorted_heights.sort(reverse=True)
        max_size=sorted_heights[0]
        heights.append(0)
        for cur_height in sorted_heights:
            print(cur_height)
            if cur_height*(len(heights)-1)<max_size:
                break
            max_consec=1
            cur_consec=0
            for i in heights:
                if i>=cur_height:
                    cur_consec=cur_consec+1
                else:
                    max_consec=max(max_consec,cur_consec)
                    cur_consec=0
            max_size=max(max_size,max_consec*cur_height)
        return max_size

    def largestRectangleArea(self, heights: List[int]) -> int:
        N, max_height = len(heights), 0
        stack = []
        for i, height in enumerate(heights + [-1]):
            start = i
            while stack and stack[-1][1] >= height:
                index, value = stack.pop()
                max_height = max(max_height, value * (i - index))
                start = index
            stack.append((start, height))

        return max_height




# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    heights =[2,1,5,6,2,3]
    solution=Solution()
    print(solution.largestRectangleArea(heights))

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
