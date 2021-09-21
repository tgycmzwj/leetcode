# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.


class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        num_paths=[[0]*n for i in range(m)]
        for i in range(len(num_paths)):
            num_paths[i][-1]=1
        for i in range(len(num_paths[0])):
            num_paths[-1][i]=1
        for i in range(m-2,-1,-1):
            for j in range(n-2,-1,-1):
                num_paths[i][j]=num_paths[i+1][j]+num_paths[i][j+1]
        return num_paths[0][0]

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    solution=Solution()
    m = 7
    n = 3
    print(solution.uniquePaths(m,n))

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
