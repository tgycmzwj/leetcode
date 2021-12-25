# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.

class MyLinkedList:
    def __init__(self):
        self.array=[]
    def get(self, index: int) -> int:
        if index<0 or index>=len(self.array):
            return -1
        return self.array[index]
    def addAtHead(self, val: int) -> None:
        self.array.insert(0,val)
    def addAtTail(self, val: int) -> None:
        self.array.append(val)
    def addAtIndex(self, index: int, val: int) -> None:
        if index<=len(self.array):
            self.array.insert(index,val)
    def deleteAtIndex(self, index: int) -> None:
        if index>=0 and index<=len(self.array)-1:
            self.array.pop(index)

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    cmds=["MyLinkedList", "addAtHead", "addAtTail", "addAtIndex", "get", "deleteAtIndex", "get"]
    vals=[[], [1], [3], [1, 2], [1], [1], [1]]
    results=[]

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
