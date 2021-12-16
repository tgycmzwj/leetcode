# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.

from typing import List
class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        results=[]
        nonprocess=set(list(range(len(isConnected))))-set([i[j] for i in results for j in len(i)])
        while len(nonprocess)!=0:
            cur_ele=nonprocess.pop()
            cur_set=[]
            to_process=[cur_ele]
            while len(to_process)!=0:
                proc=to_process.pop(0)
                for i in range(len(isConnected[proc])):
                    if isConnected[proc][i]==1 and i not in cur_set:
                        to_process.append(i)
                        cur_set.append(i)
            results.append(cur_set.copy())
            nonprocess = set(list(range(len(isConnected)))) - set([i[j] for i in results for j in range(len(i))])
        return len(results)







# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    isConnected = [[1,1,0],[1,1,0],[0,0,1]]
    isConnected = [[1, 0, 0], [0, 1, 0], [0, 0, 1]]
    isConnected=[[1,0,0,1],[0,1,1,0],[0,1,1,1],[1,0,1,1]]
    solution=Solution()
    print(solution.findCircleNum(isConnected))

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
