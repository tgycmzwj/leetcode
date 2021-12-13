# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.
from typing import List
class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        results=[""+str(i) if ((i%3!=0) and (i%5!=0)) else "" for i in range(1,n+1)]
        for i in range(1,n+1):
            if i%3==0:
                results[i-1]=results[i-1]+'Fizz'
            if i%5==0:
                results[i-1]=results[i-1]+'Buzz'
        return results




# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    n = 15
    solution=Solution()
    print(solution.fizzBuzz(n))

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
