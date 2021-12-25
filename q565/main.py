# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.

from typing import List
class Solution:
    def arrayNesting(self, nums: List[int]) -> int:
        cur_max=0
        for i in range(len(nums)):
            #already seen
            if nums[i]=='?':
                continue
            length=0
            #note that this is a permutation, no need to worry about out of bound
            while nums[i]!='?':
                nums[i],i='?',nums[i]
                length=length+1
            if length>cur_max:
                cur_max=length
        return cur_max


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    nums = [5, 4, 0, 3, 1, 6, 2]
    solution=Solution()
    print(solution.arrayNesting(nums))

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
