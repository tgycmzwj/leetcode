# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.

from typing import List
class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        total_index=0
        results=[]
        while len(results)==0:
            for i in range(min(total_index+1,len(list1))):
                j=total_index-i
                if j<=len(list2)-1:
                    if list1[i]==list2[j]:
                        results.append(list1[i])
            total_index=total_index+1
        return results

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    list1 = ["Shogun","Tapioca Express","Burger King","KFC"]
    list2 = ["Piatti","The Grill at Torrey Pines","Hungry Hunter Steakhouse","Shogun"]
    list1=["Shogun", "Tapioca Express", "Burger King", "KFC"]
    list2=["KNN", "KFC", "Burger King", "Tapioca Express", "Shogun"]
    solution=Solution()
    print(solution.findRestaurant(list1,list2))

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
