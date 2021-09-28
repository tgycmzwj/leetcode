# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.
from typing import List
class NumArray:
    def __init__(self, nums: List[int]):
        self.nums=nums
    def sumRange(self, left: int, right: int) -> int:
        return sum(self.nums[left:right+1])


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    cmds_cont=["NumArray", "sumRange", "sumRange", "sumRange"]
    cmds_value=[[[-2, 0, 3, -5, 2, -1]], [0, 2], [2, 5], [0, 5]]
    results=[]
    for i in range(len(cmds_cont)):
        cmd_cont,cmd_value=cmds_cont[i],cmds_value[i]
        if cmd_cont=='NumArray':
            obj=NumArray(cmd_value[0])
            results.append(None)
        elif cmd_cont=='sumRange':
            results.append(obj.sumRange(cmd_value[0],cmd_value[1]))
    print(results)


# See PyCharm help at https://www.jetbrains.com/help/pycharm/
