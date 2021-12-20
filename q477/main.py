# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.

from typing import List
class Solution:
    def totalHammingDistance(self, nums: List[int]) -> int:
        length=len(str(bin(max(nums)))[2:])
        nums=[str(bin(ele))[2:].zfill(length) for ele in nums]
        results=0
        for i in range(length):
            results=results+''.join([ele[i] for ele in nums]).count('0')*''.join([ele[i] for ele in nums]).count('1')
        return results


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    nums = [4,14,2]
    solution=Solution()
    print(solution.totalHammingDistance(nums))

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
