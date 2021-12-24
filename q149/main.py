# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.

from typing import List
class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        leng=len(points)
        cur_max=0
        for i in range(leng):
            counter=1
            dic={'placeholder':0}
            for j in range(i+1,leng):
                x1,y1,x2,y2=points[i][0],points[i][1],points[j][0],points[j][1]
                #case1: two points are the same
                if x1==x2 and y1==y2:
                    counter=counter+1
                    continue
                #case2: slope is infinite
                elif x1==x2:
                    slope='i'
                #case3: finite slope
                else:
                    slope=(y2-y1)/(x2-x1)
                if slope not in dic:
                    dic[slope]=0
                dic[slope]+=1
            cur_max=max(cur_max,max(dic.values())+counter)
        return cur_max




# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    points = [[1,1],[3,2],[5,3],[4,1],[2,3],[1,4]]
    solution=Solution()
    print(solution.maxPoints(points))

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
