# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.

class MyCircularQueue:
    def __init__(self, k: int):
        self.cap=k
        self.cont=[]
    def enQueue(self, value: int) -> bool:
        if len(self.cont)<self.cap:
            self.cont.append(value)
            return True
        return False
    def deQueue(self) -> bool:
        if len(self.cont)>0:
            self.cont=self.cont[1:]
            return True
        return False
    def Front(self) -> int:
        if len(self.cont)>0:
            return self.cont[0]
        return -1
    def Rear(self) -> int:
        if len(self.cont)>0:
            return self.cont[-1]
        return -1
    def isEmpty(self) -> bool:
        return len(self.cont)==0
    def isFull(self) -> bool:
        return len(self.cont)==self.cap

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    cmds=["MyCircularQueue", "enQueue", "enQueue", "enQueue", "enQueue", "Rear", "isFull", "deQueue", "enQueue", "Rear"]
    vals=[[3], [1], [2], [3], [4], [], [], [], [4], []]
    cmds=["MyCircularQueue", "enQueue", "enQueue", "enQueue", "enQueue", "deQueue", "deQueue", "isEmpty", "isEmpty", "Rear",
     "Rear", "deQueue"]
    vals=[[8], [3], [9], [5], [0], [], [], [], [], [], [], []]
    results=[]
    obj=MyCircularQueue(1)
    for i in range(len(cmds)):
        cmd,val=cmds[i],vals[i]
        if cmd=='MyCircularQueue':
            obj=MyCircularQueue(val[0])
            results.append(None)
        elif cmd=='enQueue':
            results.append(obj.enQueue(val[0]))
        elif cmd=='deQueue':
            results.append(obj.deQueue())
        elif cmd=='Rear':
            results.append(obj.Rear())
        elif cmd=='isFull':
            results.append(obj.isFull())
        elif cmd=='isEmpty':
            results.append(obj.isEmpty())
        elif cmd=='Front':
            results.append(obj.Front())
    print(results)


# See PyCharm help at https://www.jetbrains.com/help/pycharm/
