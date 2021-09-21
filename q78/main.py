# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.
from typing import List

class Solution:
    def combination(self,list,k):
        if k==1:
            return [[i] for i in list]
        if k==len(list):
            return [list]
        short_results=self.combination(list[:-1],k-1)
        long_results=self.combination(list[:-1],k)
        for i in short_results:
            i.append(list[-1])
        return short_results+long_results
    def subsets(self, nums: List[int]) -> List[List[int]]:
        results=[[]]
        for i in range(1,len(nums)+1):
            temp=self.combination(nums,i)
            for j in temp:
                results.append(j)
        return results

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    nums = [1,2,3]
    solution=Solution()
    print(solution.subsets(nums))


# See PyCharm help at https://www.jetbrains.com/help/pycharm/
