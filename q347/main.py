# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.
from typing import List
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dic={}
        for i in nums:
            if i in dic:
                dic[i]+=1
            else:
                dic[i]=1
        results=list(dic.items())
        results=sorted(results,key=lambda x:x[1],reverse=True)
        return [results[i][0] for i in range(len(results)) if i<k]

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    nums = [1,1,1,2,2,3]
    k = 2
    solution=Solution()
    print(solution.topKFrequent(nums,k))

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
