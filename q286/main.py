# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.

from typing import List
class Solution:
    def wallsAndGates(self, rooms: List[List[int]]) -> None:
        ## Find all starting points
        n, m = len(rooms), len(rooms[0])
        queue = []
        for i in range(n):
            for j in range(m):
                if rooms[i][j] == 0:
                    queue.append((i,j,0))
        ## BFS
        while queue:
            x, y, d = queue.pop(0)
            for dx,dy in [(-1,0),(1,0),(0,-1),(0,1)]:
                x_new,y_new=x+dx,y+dy
                if 0<=x_new<n and 0<=y_new<m and d+1<rooms[x_new][y_new]:
                    rooms[x_new][y_new]=d+1
                    queue.append((x_new,y_new,d+1))



# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    rooms = [[2147483647,-1,0,2147483647],[2147483647,2147483647,2147483647,-1],[2147483647,-1,2147483647,-1],[0,-1,2147483647,2147483647]]
    solution=Solution()
    print(solution.wallsAndGates(rooms))

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
