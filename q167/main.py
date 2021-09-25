# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.

from typing import List
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        for i in range(len(numbers)-1):
            if i<len(numbers)-2:
                if numbers[i]==numbers[i+2]:
                    continue
            for j in range(i+1,len(numbers)):
                if j<len(numbers)-1:
                    if numbers[j]==numbers[j+1]:
                        continue
                if numbers[i]+numbers[j]==target:
                    return [i+1,j+1]

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    solution=Solution()
    numbers = [2, 7, 11, 15]
    target = 9
    numbers=[0,0,3,4]
    target=0
    print(solution.twoSum(numbers,target))

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
