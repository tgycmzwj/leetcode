# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.


class Solution:
    def rotatedDigits(self, N: int) -> int:
        count = 0
        for d in range(1, N+1):
            d = str(d)
            if '3' in d or '4' in d or '7' in d:
                continue
            if '2' in d or '5' in d or '6' in d or '9' in d:
                count+=1
        return count

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    n=100
    solution=Solution()
    print(solution.rotatedDigits(n))

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
