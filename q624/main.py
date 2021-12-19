# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.

from typing import List


class Solution:
    def maxDistance(self, arrays: List[List[int]]) -> int:
        global_min, index_min = min((array[0], index) for index, array in enumerate(arrays))
        global_max, index_max = max((array[-1], index) for index, array in enumerate(arrays))

        if index_min != index_max:
            return global_max - global_min

        second_min, index_second_min = min(
            (array[0], index) for index, array in enumerate(arrays) if index != index_min)
        second_max, index_second_max = max(
            (array[-1], index) for index, array in enumerate(arrays) if index != index_max)

        return max(abs(global_max - second_min), abs(second_max - global_min))



# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    arrays = [[1,2,3],[4,5],[1,2,3]]
    solution=Solution()
    print(solution.maxDistance(arrays))

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
