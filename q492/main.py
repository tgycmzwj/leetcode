# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.
from typing import List
class Solution:
    def constructRectangle(self, area: int) -> List[int]:
        all_factors=[i for i in range(1,int(pow(area,0.5)+1)) if area%i==0]
        return [area//all_factors[-1],all_factors[-1]]


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    area=122122
    solution=Solution()
    print(solution.constructRectangle(area))

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
