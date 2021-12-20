# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.


class Solution:
    def parseTernary(self, expression: str) -> str:
        stack = [expression[-1]]
        for i in range(len(expression)-3, -1, -2):
            if expression[i + 1] == '?':
                if expression[i] == 'T':
                    stack.pop(-2)
                else:
                    stack.pop(-1)
            else:
                stack.append(expression[i])
        return stack.pop()


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    expression = "F?1:T?4:5"
    expression = "T?T?F:5:3"
    solution=Solution()
    print(solution.parseTernary(expression))

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
