# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.

from typing import List
class Solution:
    def can(self,i):
        if self.flowerbed[i]==1:
            return False
        if i==0:
            if self.flowerbed[i+1]==0:
                self.flowerbed[i]=1
                return True
            return False
        elif i==len(self.flowerbed)-1:
            if self.flowerbed[-2]==0:
                self.flowerbed[-1]=1
                return True
            return False
        if self.flowerbed[i-1]+self.flowerbed[i+1]==0:
            self.flowerbed[i]=1
            return True
        return False
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        if len(flowerbed)==1:
            return ((sum(flowerbed)==0 and n==1) or (n==0))
        self.flowerbed=flowerbed
        counter=0
        for i in range(len(self.flowerbed)):
            if self.can(i):
                counter=counter+1
        if counter >= n:
            return True
        return False

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    flowerbed = [1,0,0,0,1]
    n = 2
    flowerbed=[1, 0]
    n=1
    solution=Solution()
    print(solution.canPlaceFlowers(flowerbed,n))

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
