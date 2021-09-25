# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.

from typing import List
class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        distance_triangle=[[0]*len(item) for item in triangle]
        distance_triangle[0][0]=triangle[0][0]
        for i in range(1,len(distance_triangle)):
            for j in range(len(distance_triangle[i])):
                if j==0:
                    distance_triangle[i][j]=distance_triangle[i-1][j]+triangle[i][j]
                elif j==len(distance_triangle[i])-1:
                    distance_triangle[i][j]=distance_triangle[i-1][j-1]+triangle[i][j]
                else:
                    distance_triangle[i][j]=min(distance_triangle[i-1][j-1],distance_triangle[i-1][j])+triangle[i][j]
        return min(distance_triangle[-1])




# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    solution=Solution()
    triangle = [[2], [3, 4], [6, 5, 7], [4, 1, 8, 3]]
    triangle = [[-10]]
    print(solution.minimumTotal(triangle))


# See PyCharm help at https://www.jetbrains.com/help/pycharm/
