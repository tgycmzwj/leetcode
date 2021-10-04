# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.
from typing import List
class Solution:
    def hIndex(self, citations: List[int]) -> int:
        n=len(citations)
        if n==0:
            return 0
        low=0
        high=n
        while high>low:
            mid=(low+high)//2
            if n-mid==citations[mid]:
                return n-mid
            if n-mid>citations[mid]:
                low=mid+1
            else:
                high=mid
        return n-low

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
if __name__ == '__main__':
    citations = [0,1,3,5,6]
    citations=[1,1,2]
    solution=Solution()
    print(solution.hIndex(citations))