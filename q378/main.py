# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.
from typing import List
class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        results=sorted([item[i] for item in matrix for i in range(len(item))])
        return results[k-1]


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    matrix = [[1,5,9],[10,11,13],[12,13,15]]
    k = 8
    solution=Solution()
    print(solution.kthSmallest(matrix,k))

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
