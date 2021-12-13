# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.

from typing import List
class Solution:
    def maxDistToClosest(self, seats: List[int]) -> int:
        length=len(seats)
        index1=[i for i in range(len(seats)) if seats[i]==1]
        side=max(index1[0],length-index1[-1]-1)
        if len(index1)==1:
            return side
        else:
            diff=[(index1[i+1]-index1[i])//2 for i in range(len(index1)-1)]
            return max(side,max(diff))


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    seats = [1, 0, 0, 0, 1, 0, 1]
    #seats = [1, 0, 0, 0]
    solution=Solution()
    print(solution.maxDistToClosest(seats))

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
