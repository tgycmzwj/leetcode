# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.

from typing import List
class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        results=[]
        for i in range(numRows):
            cur_list=[1]
            for j in range(i-1):
                cur_list.append(pre_list[j]+pre_list[j+1])
            if i>0:
                cur_list.append(1)
            results.append(cur_list)
            pre_list=cur_list
        return results


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    numRows = 1
    solution=Solution()
    print(solution.generate(numRows))

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
