# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.
from typing import List
class Solution:
    def anagramMappings(self, nums1: List[int], nums2: List[int]) -> List[int]:
        ans=[]
        n = len(nums1)
        for i in range(n):
            ans.append(nums2.index(nums1[i]))
        return ans

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    nums1 = [12,28,46,32,50]
    nums2 = [50,12,32,46,28]
    solution=Solution()
    print(solution.anagramMappings(nums1,nums2))

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
