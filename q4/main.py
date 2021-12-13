from typing import List
class Solution:
    def ksmallest(self,nums1:List[int],nums2:List[int],k)->int:
        if not nums1:
            return nums2[k]
        if not nums2:
            return nums1[k]
        midindex1,midindex2=len(nums1)//2,len(nums2)//2
        mid1,mid2=nums1[midindex1],nums2[midindex2]
        if k>midindex1+midindex2:
            if mid1<mid2:
                return self.ksmallest(nums1[midindex1+1:],nums2,k-midindex1-1)
            else:
                return self.ksmallest(nums1,nums2[midindex2+1:],k-midindex2-1)
        else:
            if mid1<mid2:
                return self.ksmallest(nums1,nums2[:midindex2],k)
            else:
                return self.ksmallest(nums1[:midindex1],nums2,k)
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        lens=len(nums1)+len(nums2)
        if lens%2==1:
            return self.ksmallest(nums1,nums2,lens//2)
        else:
            return (self.ksmallest(nums1,nums2,lens//2-1)+self.ksmallest(nums1,nums2,lens//2))/2.0
if __name__=='__main__':
    solution=Solution()
    nums1 = []
    nums2 = [3, 4]
    print(solution.findMedianSortedArrays(nums1,nums2))