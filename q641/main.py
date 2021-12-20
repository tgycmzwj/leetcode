# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.


class MyCircularDeque:
    def __init__(self, k: int):
        self.k=k
        self.lst=[]
    def insertFront(self, value: int) -> bool:
        if len(self.lst)==self.k:
            return False
        self.lst=[value]+self.lst
        return True
    def insertLast(self, value: int) -> bool:
        if len(self.lst)==self.k:
            return False
        self.lst.append(value)
        return True
    def deleteFront(self) -> bool:
        if len(self.lst)==0:
            return False
        self.lst.pop(0)
        return True
    def deleteLast(self) -> bool:
        if len(self.lst)==0:
            return False
        self.lst.pop(-1)
        return True
    def getFront(self) -> int:
        if len(self.lst)==0:
            return -1
        return self.lst[0]
    def getRear(self) -> int:
        if len(self.lst)==0:
            return -1
        return self.lst[-1]
    def isEmpty(self) -> bool:
        return len(self.lst)==0
    def isFull(self) -> bool:
        return len(self.lst)==self.k

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    cmds=["MyCircularDeque", "insertLast", "insertLast", "insertFront", "insertFront", "getRear", "isFull", "deleteLast",
     "insertFront", "getFront"]
    vals=[[3], [1], [2], [3], [4], [], [], [], [4], []]

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
