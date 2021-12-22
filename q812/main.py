# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.

from typing import List
class Solution:
    def largestTriangleArea(self, points: List[List[int]]) -> float:
        curmax=0
        leng=len(points)
        for i in range(leng-2):
            x1,y1=points[i][0],points[i][1]
            for j in range(i+1,leng-1):
                x2,y2=points[j][0],points[j][1]
                for k in range(j+1,leng):
                    x3,y3=points[k][0],points[k][1]
                    curmax=max(curmax,abs((x1 * (y2 - y3) + x2 * (y3 - y1)
                + x3 * (y1 - y2)) / 2.0))
        return curmax

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    points = [[0,0],[0,1],[1,0],[0,2],[2,0]]
    solution=Solution()
    print(solution.largestTriangleArea(points))

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
