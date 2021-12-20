# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.

from typing import List
class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        results=[(abs(arr[i]-x),arr[i]) for i in range(len(arr))]
        results=sorted(results,key=lambda x:(x[0],x[1]))
        return sorted([item[1] for item in results[:k]])

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    arr = [1,2,3,4,5]
    k = 4
    x = 3
    solution=Solution()
    print(solution.findClosestElements(arr,k,x))

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
