# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.


class Solution:
    def judgeCircle(self, moves: str) -> bool:
        dic = {'L': 0, 'R': 0, 'U': 0, 'D': 0}
        for i in moves:
            dic[i] = dic[i] + 1
        return dic['L'] - dic['R'] == 0 and dic['U'] - dic['D'] == 0


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    moves = "UD"
    solution=Solution()
    print(solution.judgeCircle(moves))

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
