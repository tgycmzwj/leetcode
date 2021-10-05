# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.

from typing import List
import random
class Solution:
    def __init__(self, nums: List[int]):
        self.nums=nums
    def pick(self, target: int) -> int:
        pos_index=[i for i in range(len(self.nums)) if self.nums[i]==target]
        random_index=random.randint(0, len(pos_index) - 1)
        return pos_index[random_index]


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    cmds_cont=["Solution", "pick", "pick", "pick"]
    cmds_value=[[[1, 2, 3, 3, 3]], [3], [1], [3]]
    results=[]
    for i in range(len(cmds_cont)):
        if cmds_cont[i]=='Solution':
            obj=Solution(cmds_value[i][0])
            results.append(None)
        else:
            results.append(obj.pick(cmds_value[i][0]))
    print(results)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
