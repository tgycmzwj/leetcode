# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.
from typing import List
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        len_nums=len(nums)
        all_longest=0
        cur_longest=0
        num_set=set(nums)
        while len(num_set)!=0:
            cur_analysis=num_set.pop()
            j=1
            while (cur_analysis-j) in num_set:
                num_set.remove(cur_analysis-j)
                cur_longest=cur_longest+1
                j=j+1
            j=1
            while (cur_analysis+j) in num_set:
                num_set.remove(cur_analysis+j)
                cur_longest=cur_longest+1
                j=j+1
            all_longest=max(all_longest,cur_longest)
            cur_longest=0
        return all_longest+1 if len_nums>0 else 0


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    nums = [100,4,200,1,3,2]
    nums = [0, 3, 7, 2, 5, 8, 4, 6, 0, 1]
    nums=[0]
    nums=[9, 1, 4, 7, 3, -1, 0, 5, 8, -1, 6]
    solution=Solution()
    print(solution.longestConsecutive(nums))

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
