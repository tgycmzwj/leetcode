# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.


class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        stack_s=[]
        stack_t=[]
        for i in s:
            if i=='#':
                if len(stack_s)>0:
                    stack_s.pop(-1)
            else:
                stack_s.append(i)
        for i in t:
            if i=='#':
                if len(stack_t)>0:
                    stack_t.pop(-1)
            else:
                stack_t.append(i)
        return ''.join(stack_s)==''.join(stack_t)
# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    s = "ab#c"
    t = "ad#c"
    solution=Solution()
    print(solution.backspaceCompare(s,t))

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
