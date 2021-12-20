# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.

from typing import List
class Solution:
    def constructArray(self, n: int, k: int) -> List[int]:
        results=[1]
        cur_round=0
        while k>1:
            if cur_round%2==0:
                new_num=results[-1]+((n-1)-cur_round)
            elif cur_round%2==1:
                new_num=results[-1]-((n-1)-cur_round)
            results.append(new_num)
            k=k-1
            cur_round=cur_round+1
        if cur_round%2==0:
            for i in range(1,n+1):
                if i not in results:
                    results.append(i)
        if cur_round%2==1:
            for i in range(n,0,-1):
                if i not in results:
                    results.append(i)
        return results

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    n = 5
    k = 2
    solution=Solution()
    print(solution.constructArray(n,k))

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
