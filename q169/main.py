# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.

from typing import List
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        counter_dict={}
        for i in nums:
            if i not in counter_dict.keys():
                counter_dict[i]=1
            else:
                counter_dict[i]=counter_dict[i]+1
        largest=nums[0]
        largest_counter=0
        for key,value in counter_dict.items():
            if value>largest_counter:
                largest=key
                largest_counter=value
        return largest


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    solution=Solution()
    nums=[3,2,3]
    nums = [2, 2, 1, 1, 1, 2, 2]
    print(solution.majorityElement(nums))


# See PyCharm help at https://www.jetbrains.com/help/pycharm/
