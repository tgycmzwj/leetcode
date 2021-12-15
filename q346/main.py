# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.


class MovingAverage:
    def __init__(self, size: int):
        self.size=size
        self.data=[]
    def next(self, val: int) -> float:
        if len(self.data)==self.size:
            self.data.pop(0)
        self.data.append(val)
        return sum(self.data)/len(self.data)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    cmds=["MovingAverage", "next", "next", "next", "next"]
    vals=[[3], [1], [10], [3], [5]]


# See PyCharm help at https://www.jetbrains.com/help/pycharm/
