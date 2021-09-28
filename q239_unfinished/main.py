# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.
from typing import List
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        results=[0]*(len(nums)-k+1)
        results[0]=max(nums[:k])
        max_loc=nums[:k].index(results[0])
        for i in range(1,len(results)):
            if max_loc>0:
                if nums[i+k-1]>=results[i-1]:
                    max_loc=k-1
                    results[i]=nums[i+k-1]
                else:
                    max_loc=max_loc-1
                    results[i]=results[i-1]
            else:
                results[i]=max(nums[i:i+k])
                max_loc=nums[i:i+k].index(results[i])
        return results


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    nums = [1,3,-1,-3,5,3,6,7]
    k = 3
    nums = [1]
    k = 1
    nums = [1, -1]
    k = 1
    nums = [9, 11]
    k = 2
    nums = [4, -2]
    k = 2
    solution=Solution()
    print(solution.maxSlidingWindow(nums,k))

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
