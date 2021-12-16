# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.
from typing import List
class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        l1,l2=len(heights),len(heights[0])
        dp_pacific=[[0]*l2 for i in range(l1)]
        dp_atlatic=[[0]*l2 for i in range(l1)]
        #initialize
        for i in range(l1):
            dp_pacific[i][0]=1
            dp_atlatic[i][-1]=1
        for j in range(l2):
            dp_pacific[0][j]=1
            dp_atlatic[-1][j]=1
        #update
        pacific_counter=1
        while pacific_counter>0:
            pacific_counter=0
            for i in range(1,l1):
                for j in range(1,l2):
                    if dp_pacific[i][j]==0:
                        if heights[i-1][j]<=heights[i][j] and dp_pacific[i-1][j]==1: #up
                            dp_pacific[i][j]=1
                            pacific_counter=1
                            continue
                        if i+1<l1 and heights[i+1][j]<=heights[i][j] and dp_pacific[i+1][j]==1: #down
                            dp_pacific[i][j]=1
                            pacific_counter=1
                            continue
                        if heights[i][j-1]<=heights[i][j] and dp_pacific[i][j-1]==1: #left
                            dp_pacific[i][j]=1
                            pacific_counter=1
                            continue
                        if j+1<l2 and heights[i][j+1]<=heights[i][j] and dp_pacific[i][j+1]==1: #right
                            dp_pacific[i][j]=1
                            pacific_counter=1
                            continue
        atlatic_counter = 1
        while atlatic_counter > 0:
            atlatic_counter = 0
            for i in range(l1-2,-1,-1):
                for j in range(l2-2,-1,-1):
                    if dp_atlatic[i][j] == 0:
                        if heights[i+1][j] <= heights[i][j] and dp_atlatic[i + 1][j] == 1:  # down
                            dp_atlatic[i][j] = 1
                            atlatic_counter = 1
                            continue
                        if i-1>=0 and heights[i - 1][j] <= heights[i][j] and dp_atlatic[i - 1][j] == 1:  # up
                            dp_atlatic[i][j] = 1
                            atlatic_counter = 1
                            continue
                        if heights[i][j+1] <= heights[i][j] and dp_atlatic[i][j+1] == 1:  # right
                            dp_atlatic[i][j] = 1
                            atlatic_counter = 1
                            continue
                        if j-1>=0 and heights[i][j-1] <= heights[i][j] and dp_atlatic[i][j-1] == 1:  # left
                            dp_atlatic[i][j] = 1
                            atlatic_counter = 1
                            continue
        results=[]
        for i in range(l1):
            for j in range(l2):
                if dp_atlatic[i][j]==1 and dp_pacific[i][j]==1:
                    results.append([i,j])
        return results

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    heights = [[1,2,2,3,5],[3,2,3,4,4],[2,4,5,3,1],[6,7,1,4,5],[5,1,1,2,4]]
    solution=Solution()
    print(solution.pacificAtlantic(heights))
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
