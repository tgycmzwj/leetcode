# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.


class Solution(object):
    def calPoints(self, ops):
        history = []
        for op in ops:
            if op == 'C':
                history.pop()
            elif op == 'D':
                history.append(history[-1] * 2)
            elif op == '+':
                history.append(history[-1] + history[-2])
            else:
                history.append(int(op))
        return sum(history)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    ops = ["5","2","C","D","+"]
    solution=Solution()
    print(solution.calPoints(ops))

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
