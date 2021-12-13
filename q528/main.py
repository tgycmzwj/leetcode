# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.
from typing import List
import random
class Solution:
    def __init__(self, w: List[int]):
        self.prob=[i/sum(w) for i in w]
        self.val=[i for i in range(len(self.prob))]
    def pickIndex(self) -> int:
        return random.choices(self.val,self.prob)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    cmds=["Solution", "pickIndex", "pickIndex", "pickIndex", "pickIndex", "pickIndex"]
    values=[[[1, 3]], [], [], [], [], []]
    results=[]
    solution=Solution(values[0][0])
    for i in range(len(cmds)):
        cmd,value=cmds[i],values[i]
        if cmd=='Solution':
            solution=Solution(value[0])
            results.append(None)
        else:
            results.append(solution.pickIndex())
    print(results)


# See PyCharm help at https://www.jetbrains.com/help/pycharm/
