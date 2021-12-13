# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.

from typing import List
class Solution:
    def readBinaryWatch(self, turnedOn: int) -> List[str]:
        time=[]
        for h in range(12):
            for m in range(60):
                if (bin(h)+bin(m)).count('1')==turnedOn:
                    time.append(f'{h}:{m:02d}')
        return time

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    turnedOn=4
    solution=Solution()
    print(solution.readBinaryWatch(turnedOn))

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
