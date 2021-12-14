# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.

from typing import List
class ZigzagIterator:
    def __init__(self, v1: List[int], v2: List[int]):
        self.pos=0
        i=0
        self.v=[]
        for i in range(min(len(v1),len(v2))):
            temp1,temp2=v1.pop(0),v2.pop(0)
            self.v.append(temp1)
            self.v.append(temp2)
        self.v=self.v+v1+v2
    def next(self) -> int:
        self.pos=self.pos+1
        return self.v[self.pos-1]
    def hasNext(self) -> bool:
        if self.pos<len(self.v):
            return True
        return False

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    v1 = [1,2]
    v2 = [3,4,5,6]
    zig=ZigzagIterator(v1,v2)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
