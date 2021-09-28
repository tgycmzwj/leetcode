# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.

from typing import List
class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        counter={}
        i=0
        for i in range(len(nums)):
            if nums[i] in counter.keys():
                counter[nums[i]]=counter[nums[i]]+1
            else:
                counter[nums[i]]=1
        results=[]
        for key,val in counter.items():
            if val>(i+1)//3:
                results.append(key)
        return results


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    nums = [3,2,3]
    nums = [1]
    nums = [1, 2]
    solution=Solution()
    print(solution.majorityElement(nums))

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
