# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.
from typing import List
class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        closest_sum=sum(nums[:3])
        for index1 in range(len(nums)-2):
            index2=index1+1
            index3=len(nums)-1
            while index2<index3:
                cur_sum=nums[index1]+nums[index2]+nums[index3]
                if cur_sum==target:
                    return target
                if abs(cur_sum-target)<abs(closest_sum-target):
                    closest_sum=cur_sum
                # while index2 < index3 and nums[index2] == nums[index2 + 1]:
                #     index2 += 1
                # while index2 < index3 and nums[index3] == nums[index3 - 1]:
                #     index3 -= 1
                if cur_sum>target:
                    index3-=1
                if cur_sum<target:
                    index2+=1
        return closest_sum



# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    solution=Solution()
    nums = [-1,0,1,1,55]
    target=3
    print(solution.threeSumClosest(nums,target))

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
