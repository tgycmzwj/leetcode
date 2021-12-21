# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.

from typing import List
class Solution:
    def findLongestChain(self, pairs: List[List[int]]) -> int:
        pairs=sorted(pairs,key=lambda x:x[1])
        results=[pairs[0]]
        i=1
        while i<len(pairs):
            if pairs[i][0]>results[-1][1]:
                results.append(pairs[i])
            i=i+1
        return len(results)

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    pairs = [[1,2],[2,3],[3,4]]
    solution=Solution()
    print(solution.findLongestChain(pairs))

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
