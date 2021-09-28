# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.

class MyQueue:
    def __init__(self):
        self.stack1=[]
        self.stack2=[]
    def push(self, x: int) -> None:
        self.stack1.append(x)
    def pop(self) -> int:
        while self.stack1:
            self.stack2.append(self.stack1.pop())
        temp = self.stack2.pop()
        while self.stack2:
            self.stack1.append(self.stack2.pop())
        return temp
    def peek(self) -> int:
        while self.stack1:
            self.stack2.append(self.stack1.pop())
        temp=self.stack2.pop()
        self.stack1.append(temp)
        while self.stack2:
            self.stack1.append(self.stack2.pop())
        return temp
    def empty(self) -> bool:
        return len(self.stack1)==0

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    cmds_cont=["MyQueue", "push", "push", "peek", "pop", "empty"]
    cmds_value=[[], [1], [2], [], [], []]
    results=[]
    for i in range(len(cmds_cont)):
        cmd_cont,cmd_value=cmds_cont[i],cmds_value[i]
        if cmd_cont=='MyQueue':
            obj=MyQueue()
            results.append(None)
        elif cmd_cont=='push':
            results.append(obj.push(cmd_value[0]))
        elif cmd_cont=='peek':
            results.append(obj.peek())
        elif cmd_cont=='pop':
            results.append(obj.pop())
        elif cmd_cont=='empty':
            results.append(obj.empty())
    print(results)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
