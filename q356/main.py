# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.
from typing import List

class Solution:
    def isReflected(self, points: List[List[int]]) -> bool:
        x=[i[0] for i in points]
        x=sorted(x)
        target=x[0]+x[-1]
        for i in range(len(points)):
            cur_point=points[i]
            reflextion=[2*target-cur_point[0],cur_point[1]]
            if reflextion not in points:
                return False
        return True


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    points = [[1,1],[-1,1]]
    solution=Solution()
    print(solution.isReflected(points))

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
