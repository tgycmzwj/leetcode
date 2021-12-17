# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.

from typing import List
class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        points=sorted(points,key=lambda x:x[1])
        counter=1
        cur_arrow=points[0][1]
        for i in range(len(points)):
            if cur_arrow<points[i][0]:
                counter=counter+1
                cur_arrow=points[i][1]
        return counter



# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    points=[[10,16],[2,8],[1,6],[7,12],[17,20],[1,120]]
    solution=Solution()
    print(solution.findMinArrowShots(points))

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
