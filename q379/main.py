# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.

class PhoneDirectory:
    def __init__(self, maxNumbers: int):
        self.maxNumbers=maxNumbers
        self.avai=set([i for i in range(self.maxNumbers)])
        self.used=set()
    def get(self) -> int:
        if len(self.avai)==0:
            return -1
        num=self.avai.pop()
        self.used.add(num)
        return num
    def check(self, number: int) -> bool:
        return number not in self.used
    def release(self, number: int) -> None:
        self.used.remove(number)
        self.avai.add(number)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    cmds=["PhoneDirectory", "get", "get", "check", "get", "check", "release", "check"]
    vals=[[3], [], [], [2], [], [2], [2], [2]]
    results=[]
    for i in range(len(cmds)):
        cmd,val=cmds[i],vals[i]

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
