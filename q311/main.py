# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.
class Solution:
    def multiply(self, A, B):
        cols = [[(j, b) for j, b in enumerate(col) if b] for col in zip(*B)]
        return [[sum(row[j]*b for j, b in col) for col in cols] for row in A]

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    mat1 = [[1,0,0],[-1,0,3]]
    mat2 = [[7,0,0],[0,0,0],[0,0,1]]
    solution=Solution()
    print(solution.multiply(mat1,mat2))

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
