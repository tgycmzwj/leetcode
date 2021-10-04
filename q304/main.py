from typing import List


class NumMatrix:
    def __init__(self, matrix: List[List[int]]):
        self.dp = [[0] * len(matrix[0]) for _ in matrix]
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                self.dp[i][j] = (0 if i - 1 < 0 else self.dp[i - 1][j]) + (0 if j - 1 < 0 else self.dp[i][j - 1]) - (
                    0 if i - 1 < 0 or j - 1 < 0 else self.dp[i - 1][j - 1]) + matrix[i][j]

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        return self.dp[row2][col2] - (0 if row1 - 1 < 0 else self.dp[row1 - 1][col2]) - (
            0 if col1 - 1 < 0 else self.dp[row2][col1 - 1]) + (
                   0 if row1 - 1 < 0 or col1 - 1 < 0 else self.dp[row1 - 1][col1 - 1])

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    cmds_cont=["NumMatrix", "sumRegion", "sumRegion", "sumRegion"]
    cmds_value=[[[[3, 0, 1, 4, 2], [5, 6, 3, 2, 1], [1, 2, 0, 1, 5], [4, 1, 0, 1, 7], [1, 0, 3, 0, 5]]], [2, 1, 4, 3],
     [1, 1, 2, 2], [1, 2, 2, 4]]
    results=[]
    for i in range(len(cmds_cont)):
        cmd_cont,cmd_value=cmds_cont[i],cmds_value[i]
        if cmd_cont=='NumMatrix':
            obj=NumMatrix(cmd_value[0])
            results.append(None)
        elif cmd_cont=='sumRegion':
            a,b,c,d=cmd_value
            results.append(obj.sumRegion(a,b,c,d))
    print(results)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
