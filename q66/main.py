# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.
from typing import List

class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        new_list=[str(i) for i in digits]
        results=str(int(''.join(new_list))+1)
        results_list=[]
        for i in range(len(results)):
            results_list.append(int(results[i]))
        return results_list


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    solution=Solution()
    digits = [4,3,2,1]
    print(solution.plusOne(digits))

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
