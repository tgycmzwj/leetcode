# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.

from typing import List
class Solution:
    results=[]
    def countBits(self, n: int) -> List[int]:
        cur_len=len(self.results)
        while n>cur_len-1:
            self.results.append(str(bin(cur_len)).count('1'))
            cur_len=cur_len+1
        return self.results[:n+1]


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    n=2
    solution=Solution()
    print(solution.countBits(n))

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
