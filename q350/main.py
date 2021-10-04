# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.
from typing import List
class Solution:
    def to_dict(self,nums:List[int]):
        results_dict={}
        for i in nums:
            if i not in results_dict.keys():
                results_dict[i]=1
            else:
                results_dict[i]=results_dict[i]+1
        return results_dict
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nums1,nums2=self.to_dict(nums1),self.to_dict(nums2)
        results=[]
        for key in nums1.keys():
            if key in nums2.keys():
                results=results+min(nums1[key],nums2[key])*[key]
        return results

if __name__ == '__main__':
    solution=Solution()
    nums1 = [1, 2, 2, 1]
    nums2 = [2, 2]
    nums1 = [4, 9, 5]
    nums2 = [9, 4, 9, 8, 4]
    print(solution.intersect(nums1,nums2))


