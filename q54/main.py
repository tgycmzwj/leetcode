# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.
from typing import List
class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        width=len(matrix[0])
        height=len(matrix)
        cur_direction='right'
        cur_row=0
        cur_col=0
        results=[]
        while len(results)<(width*height):
            results.append((cur_row,cur_col))
            if cur_direction=='right':
                if ((cur_col<width-1) and ((cur_row,cur_col+1) not in results)):
                    cur_col=cur_col+1
                else:
                    cur_direction='down'
                    cur_row=cur_row+1
            elif cur_direction=='down':
                if ((cur_row<height-1) and (cur_row+1,cur_col) not in results):
                    cur_row=cur_row+1
                else:
                    cur_direction='left'
                    cur_col=cur_col-1
            elif cur_direction=='left':
                if ((cur_col>0) and (cur_row,cur_col-1) not in results):
                    cur_col=cur_col-1
                else:
                    cur_direction='up'
                    cur_row=cur_row-1
            else:
                if ((cur_row>0) and (cur_row-1,cur_col) not in results):
                    cur_row=cur_row-1
                else:
                    cur_direction='right'
                    cur_col=cur_col+1
        act_results=[]
        for item in results:
            act_results.append(matrix[item[0]][item[1]])
        return act_results



# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    solution=Solution()
    matrix = [[1]]
    print(solution.spiralOrder(matrix))


# See PyCharm help at https://www.jetbrains.com/help/pycharm/
