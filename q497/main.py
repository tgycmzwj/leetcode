# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.

from typing import List

import random
class Solution:
    def __init__(self, rects: List[List[int]]):
        self.rects=rects
    def pick(self) -> List[int]:
        num=random.randint(0,len(self.rects)-1)
        x=random.randint(self.rects[num][0],self.rects[num][2])
        y=random.randint(self.rects[num][1],self.rects[num][3])
        return [x,y]



# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    cmds=["Solution", "pick", "pick", "pick", "pick", "pick"]
    vals=[[[[-2, -2, 1, 1], [2, 2, 4, 6]]], [], [], [], [], []]
    results=[]
    for i in range(len(cmds)):
        cmd,val=cmds[i],vals[i]
        if cmd=='Solution':
            obj=Solution(val[0])
            results.append(None)
        elif cmd=='pick':
            results.append(obj.pick())
    print(results)
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
