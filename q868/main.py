# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.


class Solution:
    def binaryGap(self, n: int) -> int:
        string = str(bin(n))[2:]
        results = []
        cur_max = 0
        for i in range(len(string)):
            if string[i] == '1':
                if len(results) > 0:
                    cur_max = max(cur_max, i - results[-1])
                results.append(i)
        return cur_max


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    n = 8
    solution=Solution()
    print(solution.binaryGap(n))

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
