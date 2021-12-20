# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.

from typing import List
class Solution:
    def bin_search(self,value,left,right,heaters):
        if value<=heaters[left]:
            return heaters[left]-value
        if value>=heaters[right]:
            return value-heaters[right]
        mid=(left+right)//2
        if right-left==1:
            return min(abs(heaters[left]-value),abs(heaters[right]-value))
        if heaters[mid]==value:
            return 0
        if heaters[mid]>value:
            return min(self.bin_search(value,left,mid-1,heaters),heaters[mid]-value)
        if heaters[mid]<value:
            return min(self.bin_search(value,mid+1,right,heaters),value-heaters[mid])
    def findRadius(self, houses: List[int], heaters: List[int]) -> int:
        houses.sort()
        heaters.sort()
        if len(heaters)==1:
            return max(abs(houses[0]-heaters[0]),abs(houses[-1]-heaters[0]))
        cur_max=0
        for i in houses:
            cur_max=max(cur_max,self.bin_search(i,0,len(heaters)-1,heaters))
        return cur_max


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    houses = [1,2,3,4]
    heaters = [1,4]
    houses=[1, 1, 1, 1, 1, 1, 999, 999, 999, 999, 999]
    heaters=[499, 500, 501]
    houses=[282475249,622650073,984943658,144108930,470211272,101027544,457850878,458777923]
    heaters=[823564440,115438165,784484492,74243042,114807987,137522503,441282327,16531729,823378840,143542612]
    solution=Solution()
    print(solution.findRadius(houses,heaters))

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
