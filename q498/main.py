# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.

from typing import List
class Solution:
    def findDiagonalOrder(self,mat:List[List[int]])->List[int]:
        max_sum=len(mat)+len(mat[0])-1
        results=[]
        for i in range(max_sum):
            if i%2==0:
                for j in range(min(i+1,len(mat[0]))):
                    if i-j>=0 and i-j<=len(mat)-1:
                        results.append(mat[i-j][j])
            if i%2==1:
                for j in range(min(i+1,len(mat))):
                    if i-j>=0 and i-j<=len(mat[0])-1:
                        results.append(mat[j][i-j])
        return results


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    mat = [[1,2,3],[4,5,6],[7,8,9]]
    solution=Solution()
    print(solution.findDiagonalOrder(mat))

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
