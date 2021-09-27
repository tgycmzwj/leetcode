# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.

from typing import List
class Solution:
    def canCompleteCircuit_slow(self, gas: List[int], cost: List[int]) -> int:
        for starting_point in range(len(gas)):
            possible=1
            #new_gas,new_cost=gas.copy(),cost.copy()
            new_gas=gas[starting_point:]+gas[:starting_point]
            new_cost=cost[starting_point:]+cost[:starting_point]
            cur_gas=new_gas.pop(0)
            cur_cost=new_cost.pop(0)
            while len(new_gas)>0 and possible==1:
                if cur_gas<cur_cost:
                    possible=0
                else:
                    cur_gas=cur_gas+new_gas.pop(0)-cur_cost
                    cur_cost=new_cost.pop(0)
            if (possible==1) and (cur_gas>=cur_cost):
                return starting_point
        return -1
    def canCompleteCircuit(self,gas:List[int],cost:List[int])->int:
        if sum(gas)<sum(cost):
            return -1
        starting,agg=0,0
        for i in range(len(gas)):
            agg=agg+gas[i]-cost[i]
            if agg<0:
                starting=i+1
                agg=0
        return starting

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    gas = [1,2,3,4,5]
    cost = [3,4,5,1,2]
    # gas = [2, 3, 4]
    # cost = [3, 4, 3]
    solution=Solution()
    print(solution.canCompleteCircuit(gas,cost))

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
