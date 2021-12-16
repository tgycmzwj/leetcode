# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.
from typing import List
class Solution:
    def findPairs(self, nums: List[int], k: int) -> int:
        if k==0:
            counter=0
            dic={}
            for i in nums:
                if i not in dic.keys():
                    dic[i]=1
                elif dic[i]==2:
                    continue
                else:
                    dic[i]=2
                    counter+=1
            return counter
        nums=sorted(list(set(nums)))
        counter=0
        for i in range(len(nums)-1):
            if nums[i]+k in nums[i+1:]:
                counter+=1
        return counter

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    nums = [3,1,4,1,5]
    k = 2
    solution=Solution()
    print(solution.findPairs(nums,k))

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
