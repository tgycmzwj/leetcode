# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.

from typing import List
class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        if len(arr)<3:return False
        flag_dec=0
        heheda=0
        for i in range(1,len(arr)):
            if arr[i]==arr[i-1]:return False
            if flag_dec==0:
                if arr[i]<arr[i-1]:
                    flag_dec=1
                    heheda=i-1
                    if heheda==0:return False
            if flag_dec==1:
                if arr[i]>=arr[i-1]:
                    return False
        if flag_dec==0:return False
        return True



# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    arr = [8,9,8,7,6,5,4,3,2,1,0]
    solution=Solution()
    print(solution.validMountainArray(arr))

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
