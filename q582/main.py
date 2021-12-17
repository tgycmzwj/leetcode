# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.

from typing import List
class Solution:
    def killProcess(self, pid: List[int], ppid: List[int], kill: int) -> List[int]:
        dic={}
        for i in range(len(ppid)):
            if ppid[i] not in dic:
                dic[ppid[i]]=[pid[i]]
            else:
                dic[ppid[i]].append(pid[i])
        results=[kill]
        process=[kill]
        while len(process)!=0:
            cur_ele=process.pop(0)
            if cur_ele not in dic:
                continue
            for new_ele in dic[cur_ele]:
                results.append(new_ele)
                if new_ele in dic:
                    process.append(new_ele)
        return results



# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    pid = [1,3,10,5]
    ppid = [3,0,5,3]
    kill = 5
    pid = [1]
    ppid = [0]
    kill = 1
    solution=Solution()
    print(solution.killProcess(pid,ppid,kill))

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
