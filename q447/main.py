# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.
from typing import List
import math
class Solution:
    def numberOfBoomerangs(self, points: List[List[int]]) -> int:
        if len(points)<=2:
            return 0
        dp=[[0]*len(points) for i in range(len(points))]
        for i in range(len(points)):
            for j in range(i,len(points)):
                dp[i][j]=pow((points[i][0]-points[j][0])**2+(points[i][1]-points[j][1])**2,0.5)
                dp[j][i]=dp[i][j]
        count=0
        for i in range(len(points)):
            values=dp[i]
            #initialize a dictionary
            dic={}
            for val in values:
                if val not in dic:
                    dic[val]=1
                else:
                    dic[val]=dic[val]+1
            for k,v in dic.items():
                if v>1:
                    count=count+math.factorial(v)/math.factorial(v-2)
        return int(count)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    points = [[0,0],[1,0],[2,0]]
    solution=Solution()
    print(solution.numberOfBoomerangs(points))

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
