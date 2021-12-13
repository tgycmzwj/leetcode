from typing import List
class Solution:
    def numberOfArithmeticSlices_slow(self, nums: List[int]) -> int:
        if len(nums)<3:
            return 0
        dp={0:[],1:[0]} #end_key: [start_key]
        for i in range(2,len(nums)):
            dp[i]=[i-1]
            for j in range(i):
                for start in dp[j]:
                    old_incre=(nums[j]-nums[start])/(j-start)
                    if old_incre==nums[i]-nums[j]:
                        if start not in dp[i]:
                            dp[i].append(start)
        return sum([len(item) for item in dp.values()])-len(dp)+1
    def numberOfArithmeticSlices(self,nums:List[int])->int:
        if len(nums)<3:
            return 0
        dp=[0]*len(nums)
        for i in range(2,len(nums)):
            if nums[i]-nums[i-1]==nums[i-1]-nums[i-2]:
                dp[i]=dp[i-1]+1
        return sum(dp)



# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    solution=Solution()
    nums = [1, 2, 3, 4]
    nums=[1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]
    print(solution.numberOfArithmeticSlices(nums))

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
