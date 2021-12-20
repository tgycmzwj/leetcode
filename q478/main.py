# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.


import random
from typing import List

class Solution:
    import math
    def __init__(self, radius: float, x_center: float, y_center: float):
        self.r = radius
        self.xc = x_center
        self.yc = y_center
    def randPoint(self) -> List[float]:
        while True:
            X = random.uniform(self.xc - self.r, self.xc + self.r)
            Y = random.uniform(self.yc - self.r, self.yc + self.r)
            c = X - self.xc
            d = Y - self.yc
            if (c ** 2 + d ** 2) < self.r ** 2:
                return [X, Y]


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    cmds=["Solution", "randPoint", "randPoint", "randPoint"]
    vals=[[1.0, 0.0, 0.0], [], [], []]

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
