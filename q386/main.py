# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.

from typing import List
class Solution:
    def lexicalOrder(self, n: int) -> List[int]:
        return [int(item) for item in sorted([str(i) for i in range(1,n)])]

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    n=13
    solution=Solution()
    print(solution.lexicalOrder(n))

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
