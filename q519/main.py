# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.
from typing import List
import random
class Solution:
    def __init__(self, m: int, n: int):
        self.m=m
        self.n=n
        self.len_range=m*n
        self.used=set()
    def flip(self) -> List[int]:
        val = random.randint(0, self.len_range-1)
        while val in self.used:
            val += 1
            if val == self.len_range:
                val = 0
        self.used.add(val)
        return list(divmod(val, self.n))
    def reset(self) -> None:
        self.used=set()

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    cmds=["Solution", "flip", "flip", "flip", "reset", "flip"]
    vals=[[3, 1], [], [], [], [], []]
    results=[]
    for i in range(len(cmds)):
        cmd,val=cmds[i],vals[i]
        if cmd=='Solution':
            obj=Solution(val[0],val[1])
            results.append(None)
        elif cmd=='flip':
            results.append(obj.flip())
        elif cmd=='reset':
            results.append(obj.reset())
    print(results)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
