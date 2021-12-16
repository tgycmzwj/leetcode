# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.
from typing import List
class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        pos_dict={}
        results=[]
        cur_len=0
        while cur_len<k:
            pos_dict[0]=[0,nums1[0]*nums2[0]]


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    nums1 = [1,7,11]
    nums2 = [2,4,6]
    k = 3
    solution=Solution()
    print(solution.kSmallestPairs(nums1,nums2,k))

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
