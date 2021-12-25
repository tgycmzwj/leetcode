# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.

from typing import List
class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        dic={5:0,10:0,20:0}
        for i in range(len(bills)):
            cur_amount=bills[i]
            exchange_amount=bills[i]-5
            while exchange_amount>0:
                if exchange_amount>=10 and dic[10]>0:
                    exchange_amount=exchange_amount-10
                    dic[10]-=1
                elif exchange_amount>=5 and dic[5]>0:
                    exchange_amount=exchange_amount-5
                    dic[5]-=1
                else:
                    return False
            dic[cur_amount]+=1
        return True

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    bills = [5,5,5,10,20]
    bills=[5,5,10,10,20]
    solution=Solution()
    print(solution.lemonadeChange(bills))

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
