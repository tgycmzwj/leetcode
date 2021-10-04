# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.
from typing import List

class Solution:
    def binary_loc(self,nums:List[int],target:int)->int:
        left=0
        right=len(nums)-1
        while right>=left:
            mid=(left+right)//2
            if nums[mid]>target:
                right=mid-1
            elif nums[mid]<target:
                left=mid+1
            else:
                return mid
        return left
    def binary_find(self,nums:List[int],target:int)->bool:
        left = 0
        right = len(nums) - 1
        while right >= left:
            mid = (left + right) // 2
            if nums[mid] > target:
                right = mid - 1
            elif nums[mid] < target:
                left = mid + 1
            else:
                return 1
        return 0
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        n_rows=len(matrix)
        n_cols=len(matrix[0])
        while n_cols>=1 and n_cols>=1:
            #search over the first and the last row
            pos_first_row=self.binary_loc(matrix[0],target)
            pos_last_row=self.binary_loc(matrix[-1],target)
            bin_first_row=self.binary_find(matrix[0],target)
            bin_last_row=self.binary_find(matrix[-1],target)
            if bin_first_row+bin_last_row>=1:
                return True
            matrix=[item[pos_last_row:pos_first_row] for item in matrix]
            n_rows=len(matrix)
            if n_rows<=1:
                break
            if type(matrix[0])=='int':
                break
            n_cols=len(matrix[0])
            if n_cols<=1:
                break
            #search over the first and the last col
            pos_first_col=self.binary_loc([item[0] for item in matrix],target)
            pos_last_col=self.binary_loc([item[-1] for item in matrix],target)
            bin_first_col = self.binary_find([item[0] for item in matrix],target)
            bin_last_col = self.binary_find([item[-1] for item in matrix],target)
            if bin_first_col+bin_last_col>=1:
                return True
            matrix=matrix[pos_last_col:pos_first_col]
            n_rows = len(matrix)
            if n_rows<=1:
                break
            if type(matrix[0])=='int':
                break
            n_cols=len(matrix[0])
            if n_cols<=1:
                break

        if len(matrix)==0:
            return False
        elif type(matrix[0])=='int':
            return self.binary_find(matrix,target)
        elif len(matrix[0])==0:
            return False
        elif len(matrix[0])==1:
            return self.binary_find([item[0] for item in matrix],target)
        else:
            return self.binary_find(matrix[0],target)
        print('hehe')


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    matrix = [[1, 4, 7, 11, 15], [2, 5, 8, 12, 19], [3, 6, 9, 16, 22], [10, 13, 14, 17, 24],
              [18, 21, 23, 26, 30]]
    target = 20
    matrix=[[1,2,3,4,5],[6,7,8,9,10],[11,12,13,14,15],[16,17,18,19,20],[21,22,23,24,25]]
    target=19
    solution=Solution()
    print(solution.searchMatrix(matrix,target))

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
