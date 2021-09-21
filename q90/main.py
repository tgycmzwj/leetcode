# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.
from typing import List

class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        all_sets=[]
        for i in range(2**len(nums)):
            cur_binary=str(bin(i))[2:].zfill(len(nums))
            cur_num=[nums[i] for i in range(len(cur_binary)) if cur_binary[i]=='1']
            cur_num.sort()
            if cur_num not in all_sets:
                all_sets.append(cur_num)
        return all_sets



# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    nums = [0]
    solution=Solution()
    print(solution.subsetsWithDup(nums))
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
