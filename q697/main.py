# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.
from typing import List

class Solution:
    def findShortestSubArray(self, nums: List[int]) -> int:
        dic={}
        maxi=0
        for i in range(len(nums)):
            if nums[i] not in dic.keys():
                dic[nums[i]]=[1,i,i]
            else:
                dic[nums[i]]=[dic[nums[i]][0]+1,dic[nums[i]][1],i]
            maxi=max(maxi,dic[nums[i]][0])
        results=len(nums)
        for k,v in dic.items():
            if v[0]==maxi:
                results=min(results,v[2]-v[1]+1)
        return results


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    nums = [1,2,2,3,1,4,2]
    solution=Solution()
    print(solution.findShortestSubArray(nums))


# See PyCharm help at https://www.jetbrains.com/help/pycharm/
