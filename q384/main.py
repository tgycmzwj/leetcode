# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.
from typing import List
import random
class Solution:
    def __init__(self, nums: List[int]):
        self.nums=nums
    def reset(self) -> List[int]:
        return self.nums
    def shuffle(self) -> List[int]:
        new_nums=self.nums.copy()
        random.shuffle(new_nums)
        return new_nums



# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
