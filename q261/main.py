# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.
from typing import List

class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        covered = []
        if len(edges) == 0:
            if n == 1:
                return True
            return False
        if len(edges) != n - 1:
            return False

        covered=[]
        pending=[edges[0][0]]
        while len(pending)!=0:
            cur_ele=pending.pop(0)
            as_head=[i[1] for i in edges if i[0]==cur_ele]
            as_tail=[i[0] for i in edges if i[1]==cur_ele]
            if len(set(as_head).intersection(set(as_tail)))>0:
                return False
            if len(set(as_head+as_tail).intersection(set(pending)))>0:
                return False
            else:
                pending=pending+as_head+as_tail
                edges=[i for i in edges if i[0]!=cur_ele and i[1]!=cur_ele]
        return True


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    n = 3
    #edges = [[0,1],[0,2],[0,3],[1,4]]
    edges=[[2,0],[2,1]]
    #edges=[[0,1],[1,2],[2,3],[1,3],[1,4]]
    solution=Solution()
    print(solution.validTree(n,edges))


# See PyCharm help at https://www.jetbrains.com/help/pycharm/
