# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.
from typing import List
class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        results=[]
        for i in range(len(nums1)):
            for j in range(nums2.index(nums1[i]),len(nums2)):
                if nums2[j]>nums1[i]:
                    results.append(nums2[j])
                    break
            if len(results)<i+1:
                results.append(-1)
        return results




# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    nums1 = [4, 1, 2]
    nums2 = [1, 3, 4, 2]
    solution=Solution()
    print(solution.nextGreaterElement(nums1,nums2))

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
