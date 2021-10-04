# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.
from typing import List
import itertools
import re
#this question is really imprecise....
class Solution:
    def operation(self,num1,num2,operator):
        if operator=='+':
            return num1+num2
        if operator=='-':
            return num1-num2
        if operator=='*':
            return num1*num2
        if operator=='/':
            return num1/num2
    def eval_exp_with_order(self,expression,order):
        operators=[i for i in expression if i in '+-*/']
        expression=re.split(r'\+|\-|\*|\\',expression)
        while len(order)!=0:
            cur_ele=min(order)
            cur_ele_loc=order.index(cur_ele)
            order.remove(cur_ele)
            temp_results=self.operation(int(expression[cur_ele_loc]),int(expression[cur_ele_loc+1]),operators[cur_ele_loc])
            operators.pop(cur_ele_loc)
            expression[cur_ele_loc]=temp_results
            expression.pop(cur_ele_loc+1)
        return expression[0]
    def diffWaysToCompute(self, expression: str) -> List[int]:
        all_operators=[i for i in expression if i in '+-*/']
        all_orders=itertools.permutations([i for i in range(len(all_operators))])
        results=[]
        for order in all_orders:
            results.append(self.eval_exp_with_order(expression,list(order)))
        return results




# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    expression = "2-1-1"
    expression = "2*3-4*5"
    solution=Solution()
    print(solution.diffWaysToCompute(expression))

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
