from typing import List
class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        cur_direction='right'
        cur_row=0
        cur_col=0
        results=[]
        while len(results)<(n*n):
            results.append((cur_row,cur_col))
            if cur_direction=='right':
                if ((cur_col<n-1) and (cur_row,cur_col+1) not in results):
                    cur_col=cur_col+1
                else:
                    cur_direction='down'
                    cur_row=cur_row+1
            elif cur_direction == 'down':
                if ((cur_row < n - 1) and (cur_row + 1, cur_col) not in results):
                    cur_row = cur_row + 1
                else:
                    cur_direction = 'left'
                    cur_col = cur_col - 1
            elif cur_direction == 'left':
                if ((cur_col > 0) and (cur_row, cur_col - 1) not in results):
                    cur_col = cur_col - 1
                else:
                    cur_direction = 'up'
                    cur_row = cur_row - 1
            else:
                if ((cur_row > 0) and (cur_row - 1, cur_col) not in results):
                    cur_row = cur_row - 1
                else:
                    cur_direction = 'right'
                    cur_col = cur_col + 1
        act_results=[[0]*n for i in range(n)]
        for i in range(len(results)):
            act_results[results[i][0]][results[i][1]]=i+1
        return act_results


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    solution=Solution()
    n=4
    print(solution.generateMatrix(n))


# See PyCharm help at https://www.jetbrains.com/help/pycharm/
