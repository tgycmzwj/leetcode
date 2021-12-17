# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.

from typing import List
class Solution:
    def findLHS(self, nums: List[int]) -> int:
        dp_equal,dp_small,dp_big=[0]*len(nums),[0]*len(nums),[0]*len(nums)
        counter={}
        cur_max=0
        for i in range(len(nums)):
            if nums[i] not in counter:
                counter[nums[i]]=1
            else:
                counter[nums[i]]=counter[nums[i]]+1
            dp_equal[i]=counter.get(nums[i],0)
            dp_big[i]=counter.get(nums[i]+1,0)
            dp_small[i]=counter.get(nums[i]-1,0)
            if dp_big[i]!=0 or dp_small[i]!=0:
                cur_max=max([cur_max,dp_big[i]+dp_equal[i],dp_small[i]+dp_equal[i]])
        return cur_max



# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    nums = [1,3,2,2,5,2,3,7]
    nums = [1,2,3,4]
    nums = [1, 1, 1, 1]
    solution=Solution()
    print(solution.findLHS(nums))

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
