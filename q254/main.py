# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.

from typing import List
import itertools
class Solution:
    def getFactors(self,n):
        results=[]
        if n<=2:
            return []
        for i in range(2,int(pow(n,0.5))+1):
            if n%i==0:
                reminder=n//i
                results.append([i,reminder])
                reminder_split=self.getFactors(reminder)
                for ele in reminder_split:
                    if ele[0]>=i:
                        results.append([i]+ele)
        return results









# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    n = 32
    solution=Solution()
    print(solution.getFactors(n))

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
