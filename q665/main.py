# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.

from typing import List
class Solution:
    def checkPossibility(self, nums: List[int]) -> bool:
        i=0
        for i in range(len(nums)-1):
            if nums[i+1]<nums[i]:
                break
        option1,option2=nums.copy(),nums.copy()
        #option1--reduce nums[i]
        if i==0:option1[0]=-1e6
        else:option1[i]=option1[i-1]
        #option2--increase nums[i+1]
        option2[i+1]=option2[i]
        counter1,counter2=0,0
        for i in range(len(nums)-1):
            if option1[i+1]<option1[i]:
                counter1=counter1+1
            if option2[i+1]<option2[i]:
                counter2=counter2+1
        return counter1==0 or counter2==0



# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    nums = [4,2,3]
    solution=Solution()
    print(solution.checkPossibility(nums))

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
