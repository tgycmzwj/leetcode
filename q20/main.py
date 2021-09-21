# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.

class Solution:
    def isValid(self, s: str) -> bool:
        stack=['$']
        for i in range(len(s)):
            if (s[i]=='(' or s[i]=='[' or s[i]=='{'):
                stack.append(s[i])
            elif s[i]==')':
                if stack[-1]=='(':
                    stack.pop(-1)
                else:
                    return False
            elif s[i]==']':
                if stack[-1]=='[':
                    stack.pop(-1)
                else:
                    return False
            else:
                if stack[-1]=='{':
                    stack.pop(-1)
                else:
                    return False
        if len(stack)==1:
            return True
        return False

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    solution=Solution()
    s = "{[]}"
    print(solution.isValid(s))

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
