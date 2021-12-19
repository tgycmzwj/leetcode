# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.


class MaxStack:
    def __init__(self):
        self.l = []
    def push(self, x):
        self.l.append(x)
    def pop(self):
        return self.l.pop()
    def top(self):
        return self.l[-1]
    def peekMax(self):
        return max(self.l)
    def popMax(self):
        self.l = self.l[::-1]
        max_num = self.l.pop(self.l.index(max(self.l)))
        self.l = self.l[::-1]
        return max_num


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    cmds=["MaxStack", "push", "push", "push", "top", "popMax", "top", "peekMax", "pop", "top"]
    vals=[[], [5], [1], [5], [], [], [], [], [], []]

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
