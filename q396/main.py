# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.
from typing import List
class Solution:
    def maxRotateFunction(self, A: List[int]) -> int:
        s, n = sum(A), len(A)
        cur_sum = sum([i * j for i, j in enumerate(A)])
        ans=cur_sum
        for i in range(n):
            cur_sum=cur_sum + s - A[n - 1 - i] * n
            ans = max(ans, cur_sum)
        return ans


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    nums = [4, 3, 2, 6]
    solution=Solution()
    print(solution.maxRotateFunction(nums))

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
