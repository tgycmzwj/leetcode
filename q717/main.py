# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.

from typing import List
class Solution:
    def isOneBitCharacter(self, bits: List[int]) -> bool:
        n = len(bits)
        i = 0
        while i<n-1:
            if bits[i] == 0:
                i+=1
            else:
                i+=2
        return i == n - 1 and bits[i] == 0

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    bits = [1,0,0]
    solution=Solution()
    print(solution.isOneBitCharacter(bits))

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
