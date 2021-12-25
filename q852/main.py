# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.

from typing import List
class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        flag_increase=1
        for i in range(1,len(arr)):
            if flag_increase==0:
                if arr[i]>arr[i-1]:
                    return False
            if arr[i]<arr[i-1]:
                return i-1

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    arr = [0,2,1,0]
    solution=Solution()
    print(solution.peakIndexInMountainArray(arr))

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
