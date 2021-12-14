# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.
from typing import List
class Vector2D:
    def __init__(self, vec: List[List[int]]):
        self.vec=[j for i in vec for j in i]
        self.pos=0
    def next(self) -> int:
        self.pos+=1
        return self.vec[self.pos-1]
    def hasNext(self) -> bool:
        return self.pos<len(self.vec)

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    cmds=["Vector2D", "next", "next", "next", "hasNext", "hasNext", "next", "hasNext"]
    vals=[[[[1, 2], [3], [4]]], [], [], [], [], [], [], []]
    results=[]
    obj=Vector2D(vals[0])
    for i in range(len(cmds)):
        if cmds[i]=='Vector2D':
            obj=Vector2D(vals[i][0])
            results.append(None)
        elif cmds[i]=='next':
            results.append(obj.next())
        elif cmds[i]=='hasNext':
            results.append(obj.hasNext())
    print(results)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
