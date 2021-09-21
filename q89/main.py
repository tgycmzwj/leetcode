# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.
from typing import  List

class Solution:
    def grayCode_binary(self, n: int) -> List[int]:
        if n==1:
            return [0,1]
        else:
            short_list=self.grayCode_binary(n-1)
            full_list_1=[10*i for i in short_list]
            full_list_2=[10*i+1 for i in short_list]
            full_list_2.reverse()
            return full_list_1+full_list_2
    def grayCode(self,n:int)->List[int]:
        results=self.grayCode_binary(n)
        results=[str(i).zfill(n) for i in results]
        return [int(str(i),2) for i in results]

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    n = 4
    solution=Solution()
    print(solution.grayCode(n))

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
