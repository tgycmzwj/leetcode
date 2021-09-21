# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.
from typing import List
class Solution:
    def binary_search(self,lst,target,left,right):
        if right-left<=1:
            if ((target==lst[left]) or (target==lst[right])):
                return True
            return False
        mid=(left+right)//2
        if target==lst[mid]:
            return True
        elif target>lst[mid]:
            return self.binary_search(lst,target,mid+1,right)
        else:
            return self.binary_search(lst,target,left,mid-1)

    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        lst=[i for j in matrix for i in j]
        return self.binary_search(lst,target,0,len(lst)-1)



# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    solution=Solution()
    matrix = [[1,3,5]]
    target = 3
    print(solution.searchMatrix(matrix,target))


# See PyCharm help at https://www.jetbrains.com/help/pycharm/
