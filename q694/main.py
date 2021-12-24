# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.
from typing import List
class Solution:
    def numDistinctIslands(self, grid: List[List[int]]) -> int:
        if not grid:return 0
        directions=[(1,0),(-1,0),(0,1),(0,-1)]
        islands=[]
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j]==1:
                    island=[[i,j]]
                    processed=[]
                    while len(island)>0:
                        cur_ele=island.pop(0)
                        grid[cur_ele[0]][cur_ele[1]]='#'
                        processed.append(cur_ele)
                        for di in directions:
                            new_ele=[cur_ele[0]+di[0],cur_ele[1]+di[1]]
                            if new_ele[0]>=0 and new_ele[0]<len(grid) and new_ele[1]>=0 and new_ele[1]<len(grid[0]) and grid[new_ele[0]][new_ele[1]]==1:
                                if new_ele not in island and new_ele not in processed:
                                    island.append(new_ele)
                    islands.append(processed.copy())
        islands=[sorted(i) for i in islands]
        islands=sorted(islands,key=lambda x:len(x))
        island_set={}
        for island in islands:
            if len(island) not in island_set:
                island_set[len(island)]=[island]
            else:
                flag=1
                for item in island_set[len(island)]:
                    cur_set = set()
                    for i in range(len(island)):
                        diff=(island[i][0]-item[i][0],island[i][1]-item[i][1])
                        if diff not in cur_set:
                            cur_set.add(diff)
                    if len(cur_set)==1:
                        flag=0
                if flag==1 and island not in island_set[len(island)]:
                    island_set[len(island)].append(island)
        num=0
        for k,v in island_set.items():
            num=num+len(v)
        return num




# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    grid = [[1,1,0,0,0],[1,1,0,0,0],[0,0,0,1,1],[0,0,0,1,1]]
    grid=[[0,0,0,0,1,0,1,1,0,0,1,0,1,1,0,1,1,1,0,1,1,1,0,1,0,0,0,0,0,0,0,0,0,1,0,0,1,1,0,0,0,1,1,1,1,1,1,0,1,1],[0,1,0,0,0,0,1,1,1,0,1,1,0,0,0,1,0,1,1,1,0,0,1,0,1,0,0,1,0,0,0,1,1,1,1,0,0,0,0,0,1,0,0,0,0,0,1,0,0,1],[1,0,0,0,0,0,0,1,1,1,1,0,1,1,0,0,0,0,1,0,0,1,0,0,1,1,1,0,0,0,0,0,1,1,1,0,0,1,1,1,0,1,1,0,1,0,1,1,1,1],[0,0,0,0,1,1,1,0,1,1,0,1,0,0,0,0,0,0,0,1,0,1,0,1,1,0,0,0,0,0,1,1,0,0,1,1,1,0,1,1,1,1,0,1,1,0,0,0,1,1],[0,0,0,0,1,1,1,1,0,1,1,0,0,1,1,1,0,1,1,1,0,1,1,0,0,0,1,0,1,1,1,1,1,0,1,1,0,1,1,0,1,0,0,0,0,0,1,0,0,1],[0,0,1,1,1,0,1,0,0,0,1,0,0,0,0,0,1,0,1,0,0,1,0,1,0,0,1,1,1,0,1,1,1,1,1,0,1,0,1,1,1,1,0,0,0,0,0,1,0,1],[0,1,0,1,0,0,1,0,0,0,0,1,1,1,1,1,0,1,1,1,1,1,0,0,0,0,1,0,0,1,0,0,1,0,0,1,0,0,1,1,0,0,0,0,1,1,0,1,1,0],[0,1,0,0,1,1,1,1,0,1,1,0,1,0,1,0,0,0,1,0,0,0,0,0,1,0,1,1,0,1,0,0,1,0,1,1,1,0,1,0,0,1,1,1,0,0,1,0,1,0],[0,1,0,0,0,0,0,0,1,0,0,0,1,0,0,0,0,1,0,1,0,1,0,0,0,1,0,0,0,1,0,1,0,0,1,0,0,0,0,0,0,1,1,0,1,0,0,1,0,0]]
    solution=Solution()
    print(solution.numDistinctIslands(grid))

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
