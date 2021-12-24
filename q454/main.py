# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.

import collections
class Solution:
    def fourSumCount(self, A, B, C, D):
        AB = collections.Counter(a+b for a in A for b in B)
        return sum(AB[-c-d] for c in C for d in D)

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    nums1 = [1,2]
    nums2 = [-2,-1]
    nums3 = [-1,2]
    nums4 = [0,2]
    solution=Solution()
    print(solution.fourSumCount(nums1,nums2,nums3,nums4))

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
