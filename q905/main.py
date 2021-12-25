# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.

from typing import List
class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        even=[]
        odd=[]
        for i in nums:
            if i%2==1:
                odd.append(i)
            else:
                even.append(i)
        return even+odd

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    nums = [3,1,2,4]
    solution=Solution()
    print(solution.sortArrayByParity(nums))

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
