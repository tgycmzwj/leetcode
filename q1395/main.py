# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.
from typing import List

class Solution:
    def numTeams(self, rating: List[int])->int:
        dp_smaller=[0 for i in range(len(rating))]
        dp_greater=[0 for i in range(len(rating))]
        for i in range(1,len(rating)):
            dp_smaller[i]=sum([rating[j]<rating[i] for j in range(i)])
            dp_greater[i]=sum([rating[j]>rating[i] for j in range(i)])
        dp_count=[0 for i in range(len(rating))]
        for i in range(2,len(rating)):
            for j in range(1,i):
                if rating[i]-rating[j]>0:
                    dp_count[i]=dp_count[i]+dp_smaller[j]
                if rating[i]-rating[j]<0:
                    dp_count[i]=dp_count[i]+dp_greater[j]
        return sum(dp_count)



# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    rating = [2, 5, 3, 4, 1]
    rating = [2, 1, 3]
    rating = [1, 2, 3, 4]
    solution=Solution()
    print(solution.numTeams(rating))

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
