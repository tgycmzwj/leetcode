# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.


from collections import deque


class MyStack:

    def __init__(self):
        """
        Initialize your data structure here.
        """

        # python natively support double-ended queue
        self.queue = deque()

    def push(self, x: int) -> None:
        """
        Push element x onto stack.
        """

        # push new element into queue's tail
        self.queue.append(x)

        # make new element on the head position by rotation
        for _ in range(len(self.queue) - 1):
            self.queue.append(self.queue.popleft())

    def pop(self) -> int:
        """
        Removes the element on top of the stack and returns that element.
        """

        # pop head element of queue
        return self.queue.popleft()

    def top(self) -> int:
        """
        Get the top element.
        """

        # return head element of queue
        return self.queue[0]

    def empty(self) -> bool:
        """
        Returns whether the stack is empty.
        """

        return (not self.queue)

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    cmds_cont=["MyStack", "push", "push", "top", "pop", "empty"]
    cmds_value=[[], [1], [2], [], [], []]
    results=[]
    for i in range(len(cmds_cont)):
        cmd_cont,cmd_value=cmds_cont[i],cmds_value[i]
        if cmd_cont=='MyStack':
            obj=MyStack()
            results.append(None)
        elif cmd_cont=='push':
            results.append(obj.push(cmd_value[0]))
        elif cmd_cont=='top':
            results.append(obj.top())
        elif cmd_cont=='pop':
            results.append(obj.pop())
        elif cmd_cont=='empty':
            results.append(obj.empty())
    print(results)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
