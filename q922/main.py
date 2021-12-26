# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.
from typing import List
class Solution:
    def sortArrayByParityII(self, nums: List[int]) -> List[int]:
        odd,even=[],[]
        for i in range(len(nums)):
            if nums[i]%2==1:
                odd.append(nums[i])
            else:
                even.append(nums[i])
        results=[]
        for i in range(len(odd)):
            results.append(even[i])
            results.append(odd[i])
        return results

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    nums = [4,2,5,7]
    solution=Solution()
    print(solution.sortArrayByParityII(nums))

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
