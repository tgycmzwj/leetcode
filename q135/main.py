# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.

from typing import List
class Solution:
    def candy(self, ratings: List[int]) -> int:
        results=[1]*len(ratings)
        for i in range(1,len(ratings)):
            if ratings[i]>ratings[i-1]:
                results[i]=results[i-1]+1
        for i in range(len(ratings)-1,0,-1):
            if ratings[i-1]>ratings[i]:
                results[i-1]=max(results[i-1],results[i]+1)
        return sum(results)

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    ratings = [1,2,2]
    solution=Solution()
    print(solution.candy(ratings))

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
