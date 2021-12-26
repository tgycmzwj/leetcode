# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.
from typing import List
class Solution:
    def fairCandySwap(self, aliceSizes: List[int], bobSizes: List[int]) -> List[int]:
        difference=(sum(aliceSizes)-sum(bobSizes))/2
        aliceSizes=set(aliceSizes)
        for candy in set(bobSizes):
            if difference+candy in aliceSizes:
                return [difference+candy,candy]

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    aliceSizes = [1,1]
    bobSizes = [2,2]
    solution=Solution()
    print(solution.fairCandySwap(aliceSizes,bobSizes))
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
