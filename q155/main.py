# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.

class MinStack:
    def __init__(self):
        self.stack=[]
        self.min=[]
    def push(self, val: int) -> None:
        self.stack.append(val)
        if len(self.min)==0:
            self.min.append(val)
        else:
            self.min.append(min(val,self.min[-1]))
    def pop(self) -> None:
        self.stack.pop()
        self.min.pop()
    def top(self) -> int:
        return self.stack[-1]
    def getMin(self) -> int:
        return self.min[-1]

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    cmds_rule=["MinStack", "push", "push", "push", "getMin", "pop", "top", "getMin"]
    cmds_value=[[], [-2], [0], [-3], [], [], [], []]
    results=[]
    for i in range(len(cmds_rule)):
        cmd_rule,cmd_value=cmds_rule[i],cmds_value[i]
        if cmd_rule=='MinStack':
            obj=MinStack()
            results.append(None)
        elif cmd_rule=='push':
            results.append(obj.push(cmd_value[0]))
        elif cmd_rule=='pop':
            results.append(obj.pop())
        elif cmd_rule=='top':
            results.append(obj.top())
        elif cmd_rule=='getMin':
            results.append(obj.getMin())
    print(results)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
