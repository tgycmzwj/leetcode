# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.

from typing import List
class Solution:
    def isRectangleOverlap(self, rec1: List[int], rec2: List[int]) -> bool:
        x_intersect=min(rec1[2],rec2[2])-max(rec1[0],rec2[0])
        y_intersect=min(rec1[3],rec2[3])-max(rec1[1],rec2[1])
        overlap=x_intersect*y_intersect if x_intersect>0 and y_intersect>0 else 0
        return overlap>0

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    rec1 = [0,0,2,2]
    rec2 = [1,1,3,3]
    solution=Solution()
    print(solution.isRectangleOverlap(rec1,rec2))

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
