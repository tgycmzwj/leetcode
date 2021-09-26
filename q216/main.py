# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.
from typing import List
class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        if n>45:
            return []
        #the dp matrix
        matrix=[[0]*k for j in range(n+1)]
        for i in range(1,n+1):
            for j in range(k):
                matrix[i][j]=[]

        #fill the border
        #use only one number
        matrix[0][0]=[[1]]
        # sum to 1 using j numbers---not possible
        for i in range(1,min(10,n+1)):
            matrix[i][0].append([i])
        for i in range(2,n+1):
            for j in range(1,k):
                for analyzing_num in range(max(1,i-9),i):
                    old_possibilities=matrix[analyzing_num][j-1]
                    for item in old_possibilities:
                        if i-analyzing_num not in item:
                            new_item=item.copy()
                            new_item.append(i-analyzing_num)
                            new_item.sort()
                            if new_item not in matrix[i][j]:
                                matrix[i][j].append(new_item)

        return matrix[n][k-1]


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    k = 9
    n = 45
    solution=Solution()
    print(solution.combinationSum3(k,n))

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
