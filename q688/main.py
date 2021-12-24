# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes,files,tool windows,actions,and settings.

import functools
class Solution:
    def travels(self,x,y,k):
        if x< 0 or x>= self.n or y< 0 or y>= self.n:
            return 0
        elif k == 0:
            return 1
        else:
            results=(self.travels(x+2,y+1,k-1)+self.travels(x+1,y+2,k-1)+self.travels(x-1,y+2,k-1)+self.travels(x-2,y+1,k-1)+
                       self.travels(x-2,y-1,k-1)+self.travels(x-1,y-2,k-1)+self.travels(x+1,y-2,k-1) + self.travels(x+2,y-1,k-1))/8
            self.dp[(x,y,k)] = results
            return results
    def knightProbability(self,N: int,K: int,r: int,c: int) -> float:
        self.dp={}
        self.n=N
        return self.travels(r,c,K)
# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    n = 3
    k =2
    row = 0
    column = 0
    solution=Solution()
    print(solution.knightProbability(n,k,row,column))

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
