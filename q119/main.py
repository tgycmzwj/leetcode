# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.


from typing import List
class Solution:
    def getRow(self, numRows: int) -> List[List[int]]:
        for i in range(numRows+1):
            cur_list=[1]
            for j in range(i-1):
                cur_list.append(pre_list[j]+pre_list[j+1])
            if i>0:
                cur_list.append(1)
            pre_list=cur_list
        return cur_list


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    numRows = 3
    solution=Solution()
    print(solution.getRow(numRows))

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
