# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.

from typing import List
class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nums1,nums2=set(nums1),set(nums2)
        return list(nums1.intersection(nums2))


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    solution=Solution()
    nums1 = [1, 2, 2, 1]
    nums2 = [2, 2]
    print(solution.intersection(nums1,nums2))

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
