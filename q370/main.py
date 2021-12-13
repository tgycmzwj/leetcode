# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.
from typing import List

class Solution:
    def getModifiedArray_slow(self, length: int, updates: List[List[int]]) -> List[int]:
        results=[0 for i in range(length)]
        for update in updates:
            left,right,val=update
            for i in range(left,right+1):
                results[i]=results[i]+val
        return results
    def getModifiedArray(self, length: int, updates: List[List[int]]) -> List[int]:
        results = [0 for i in range(length)]
        for update in updates:
            left, right, val = update
            results[left]=results[left]+val
            if right+1<length:
                results[right+1]=results[right+1]-val
        ret, prefix = [], 0
        for i in range(len(results)):
            prefix += results[i]
            ret.append(prefix)
        return ret

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    length = 5
    updates = [[1,3,2],[2,4,3],[0,2,-2]]
    length = 10
    updates = [[2, 4, 6], [5, 6, 8], [1, 9, -4]]
    solution=Solution()
    print(solution.getModifiedArray(length,updates))

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
