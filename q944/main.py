# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.

from typing import List
class Solution(object):
    def minDeletionSize(self, A):
        ret = 0
        for c in zip(*A):
            if list(c) != sorted(c):
                ret += 1
        return ret

    # Press the green button in the gutter to run the script.
if __name__ == '__main__':
    strs = ["cba","daf","ghi"]
    solution=Solution()
    print(solution.minDeletionSize(strs))

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
