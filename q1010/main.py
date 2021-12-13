# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.

from typing import List
class Solution:
    def numPairsDivisibleBy60(self, time: List[int]) -> int:
        time=[i%60 for i in time]
        counter={}
        for i in range(60):
            counter[i]=0
        for i in time:
            counter[i]=counter[i]+1
        tot=0
        for i in range(1,30):
            tot=tot+counter[i]*counter[60-i]
        tot=tot+counter[30]*(counter[30]-1)/2+counter[0]*(counter[0]-1)/2
        return int(tot)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    time = [30, 20, 150, 100, 40]
    solution=Solution()
    print(solution.numPairsDivisibleBy60(time))

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
