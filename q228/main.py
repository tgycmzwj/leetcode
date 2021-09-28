# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.

from typing import List
class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        results=[]
        if len(nums)==0:
            return results
        else:
            left_element=nums[0]
            cur_element=nums[0]
            i=0
            for i in range(1,len(nums)):
                if nums[i]-cur_element==1:
                    cur_element=nums[i]
                else:
                    if left_element!=nums[i-1]:
                        results.append(str(left_element)+'->'+str(nums[i-1]))
                    else:
                        results.append(str(left_element))
                    left_element=nums[i]
                    cur_element=nums[i]
            if i==len(nums)-1:
                if left_element!=nums[i]:
                    results.append(str(left_element)+'->'+str(nums[i]))
                else:
                    results.append(str(left_element))
        return results


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    nums = [0,2,3,4,6,8,9]
    #nums=[]
    #nums=[0, 1, 2, 4, 5, 7]
    #nums=[-1]
    solution=Solution()
    print(solution.summaryRanges(nums))

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
