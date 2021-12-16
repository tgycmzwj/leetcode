# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.

from typing import List
class Solution:
    def findLonelyPixel(self, picture: List[List[str]]) -> int:
        dp=[[0]*len(picture[0]) for i in range(len(picture))]
        row=[0]*len(picture)
        col=[0]*len(picture[0])
        for i in range(len(picture)):
            for j in range(len(picture[0])):
                dp[i][j]=(picture[i][j]=='B')
        for i in range(len(picture)):
            row[i]=sum(dp[i])
        for j in range(len(picture[0])):
            col[j]=sum([dp[i][j] for i in range(len(dp))])
        counter=0
        for i in range(len(dp)):
            if row[i]==1:
                for j in range(len(dp[0])):
                    if col[j]==1:
                        if dp[i][j]==1:
                            counter=counter+1
        return counter

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    picture = [["B","B","B"],["B","B","W"],["B","B","B"]]
    picture = [["W", "W", "B"], ["W", "B", "W"], ["B", "W", "W"]]
    solution=Solution()
    print(solution.findLonelyPixel(picture))

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
