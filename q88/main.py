# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.
from typing import List
class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        for i in range(m,len(nums1)):
            nums1[i]='na'
        i=0
        while (i<m+n) and len(nums2)>0:
            if nums1[i]=='na':
                nums1[i]=nums2[0]
                nums2.pop(0)
            elif nums1[i]>nums2[0]:
                cur_ele=nums2.pop(0)
                nums1[i+1:]=nums1[i:-1]
                nums1[i]=cur_ele
            i=i+1
        print('hehe')



# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    nums1=[-1, 0, 0, 3, 3, 3, 0, 0, 0]
    m=6
    nums2=[1, 2, 2]
    n=3
    solution=Solution()
    print(solution.merge(nums1,m,nums2,n))


# See PyCharm help at https://www.jetbrains.com/help/pycharm/
