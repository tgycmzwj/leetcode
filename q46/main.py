# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.
from typing import List
class Solution:
    def uniq(lst):
        last = object()
        for item in lst:
            if item == last:
                continue
            yield item
            last = item
    def permute(self, nums: List[int]) -> List[List[int]]:
        if len(nums)==0:
            return nums
        if len(nums)==1:
            return [nums]
        if len(nums)==2:
            return [nums,[nums[1],nums[0]]]
        results=[]
        recur_results=self.permute(nums[:-1])
        for i in range(len(recur_results)):
            for j in range(len(recur_results[i])+1):
                results.append(recur_results[i][:j]+[nums[-1]]+recur_results[i][j:])
        return [list(x) for x in set(tuple(x) for x in results)]



# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    solution=Solution()
    nums = [4,5,6,2]
    print(solution.permute(nums))

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
