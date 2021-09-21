# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.

from typing import List


class Solution:
    def combination(self,list,k):
        if k==1:
            return [[i] for i in list]
        if k==len(list):
            return [list]
        short_results=self.combination(list[:-1],k-1)
        long_results=self.combination(list[:-1],k)
        for i in short_results:
            i.append(list[-1])
        return short_results+long_results
    def combine(self, n: int, k: int) -> List[List[int]]:
        list=[i for i in range(1,n+1)]
        return self.combination(list,k)

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    solution=Solution()
    n = 1
    k = 1
    print(solution.combine(n,k))

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
