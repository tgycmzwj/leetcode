# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.
from typing import List

class Solution:
    def canPartition_slow(self, nums: List[int]) -> bool:
        total_sum=sum(nums)
        if total_sum%2==1:
            return False
        dp={0:[nums]}
        nums_uni=list(set(nums))
        for i in range(1,total_sum//2+1):
            dp[i]=[]
            for num in nums_uni:
                if i-num>=0:
                    for item in dp[i-num]:
                        if num in item:
                            temp=item.copy()
                            temp.remove(num)
                            if temp not in dp[i]:
                                dp[i].append(temp)
        if len(dp[total_sum//2])>=1:
            return True
        return False

    def canPartition(self, nums: List[int]) -> bool:
        total_sum = sum(nums)
        if total_sum % 2 == 1:
            return False
        dp=[1]+[0]*(total_sum//2)
        for num in nums:
            #每次使用一个数字，需要倒序来确保这个数字不被使用多次
            for i in range(total_sum//2,num-1,-1):
                dp[i]=dp[i] or dp[i-num]
        return dp[-1]==1
# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    nums = [1,5,11,9]
    solution=Solution()
    print(solution.canPartition(nums))

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
