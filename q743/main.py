# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.

from typing import List
class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        dic={k:0}
        flag=1
        process=[[k]]
        while flag:
            flag=0
            cur_level=process.pop(0)
            next_level=[]
            for cur_ele in cur_level:
                as_starts=[time for time in times if time[0]==cur_ele]
                for as_start in as_starts:
                    if as_start[1] not in dic or dic[as_start[1]]>dic[cur_ele]+as_start[2]:
                        dic[as_start[1]]=dic[cur_ele]+as_start[2]
                        flag=1
                        next_level.append(as_start[1])
            process.append(next_level.copy())
        return max(dic.values())



# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    times = [[2,1,1],[2,3,1],[3,4,1]]
    n = 4
    k = 2
    solution=Solution()
    print(solution.networkDelayTime(times,n,k))

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
