# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.

from typing import List
class Solution:
    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
        if r * c != len(mat) * len(mat[0]):
            return mat
        all_nums = [mat[i][j] for i in range(len(mat)) for j in range(len(mat[0]))]
        results = []
        for i in range(r):
            cur_ele = all_nums[i * c:(i + 1) * c]
            results.append(cur_ele.copy())
        return results


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    mat = [[1, 2], [3, 4]]
    r = 1
    c = 4
    solution=Solution()
    print(solution.matrixReshape(mat,r,c))

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
