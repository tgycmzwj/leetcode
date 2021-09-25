# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.

from typing import List
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack=[]
        for i in range(len(tokens)):
            if tokens[i] not in '+-*/':
                stack.append(tokens[i])
            else:
                num1=stack.pop(-1)
                num2=stack.pop(-1)
                if tokens[i]=='+':
                    stack.append(int(num1)+int(num2))
                elif tokens[i]=='-':
                    stack.append(int(num2)-int(num1))
                elif tokens[i]=='*':
                    stack.append(int(num1)*int(num2))
                else:
                    stack.append(int(num2)/int(num1))
        return stack[0]



# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    tokens = ["2","1","+","3","*"]
    solution=Solution()
    print(solution.evalRPN(tokens))

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
