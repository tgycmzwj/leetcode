# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.

from typing import List
class Solution:
    def containsNearbyAlmostDuplicate(self, nums, k, t):
        #bracket number, position number
        buckets = {0: {0:nums[0]} }
        for i in range(1,len(nums)):
            bucket_num=(nums[i]-nums[0])//(t+1)
            if bucket_num in buckets.keys():
                for pos,val in buckets[bucket_num].items():
                    if (i-pos)<=k:
                        return True
            if bucket_num+1 in buckets.keys():
                for pos,val in buckets[bucket_num+1].items():
                    if (i-pos<=k) and (val-nums[i]<=t):
                        return True
            if bucket_num-1 in buckets.keys():
                for pos,val in buckets[bucket_num-1].items():
                    if (i-pos<=k) and (nums[i]-val<=t):
                        return True
            buckets[bucket_num]={i:nums[i]}
        return False




# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    nums = [1,5,9,1,5,9]
    k = 2
    t = 3
    nums=[2147483646, 2147483647]
    k=3
    t=3
    nums=[3, 6, 0, 4]
    k=2
    t=2
    solution=Solution()
    print(solution.containsNearbyAlmostDuplicate(nums,k,t))

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
