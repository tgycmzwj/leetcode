# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.

from typing import List
class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        start=[edges[0][0],edges[0][1]]
        flag=0
        while flag==0:
            last_ledge=[start[-2],start[-1]]
            for edge in edges:
                if edge[0]==start[-1]:
                    if edge[1]!=start[-2]:
                        if edge[1] in start:
                            start.append(edge[1])
                            flag=1
                            break
                        else:
                            start.append(edge[1])
                if edge[1]==start[-1]:
                    if edge[0]!=start[-2]:
                        if edge[0] in start:
                            start.append(edge[0])
                            flag=1
                            break
                        else:
                            start.append(edge[0])
        idx=start.index(start[-1])
        start=start[idx:]
        for item in edges[::-1]:
            if item[0] in start and item[1] in start:
                return item





# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    edges = [[1,2],[2,3],[3,4],[1,4],[1,5]]
    edges=[[1,3],[3,4],[1,5],[3,5],[2,3]]
    solution=Solution()
    print(solution.findRedundantConnection(edges))

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
