# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.
import random
from random import choice
class RandomizedSet:
    def __init__(self):
        self.arr = []
        self.dict = {}
    def insert(self, val: int) -> bool:
        if val in self.dict:
            return False
        self.arr.append(val)
        self.dict[val] = len(self.arr) - 1
        return True
    def remove(self, val: int) -> bool:
        if val not in self.dict:
            return False
        idx = self.dict[val]
        self.arr[idx], self.arr[-1] = self.arr[-1], self.arr[idx]
        self.dict[self.arr[idx]] = idx
        del self.dict[self.arr.pop()]
        return True
    def getRandom(self) -> int:
        return choice(self.arr)
# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
