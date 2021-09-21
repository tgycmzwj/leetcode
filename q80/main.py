# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.

from typing import List
class Solution:
    def removeDuplicates(self, nums) -> int:
        prev = nums[0]
        count = 1
        idx = 1
        while idx < len(nums):
            if nums[idx] == prev:
                if count < 2:
                    count += 1
                    idx += 1
                else:
                    nums.pop(idx)
            else:
                prev = nums[idx]
                count = 1
                idx += 1
        return idx

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    solution=Solution()
    nums = [1,1,1,2,2,3]
    print(solution.removeDuplicates(nums))


# See PyCharm help at https://www.jetbrains.com/help/pycharm/
