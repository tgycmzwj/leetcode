# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.


class Solution:
    def countPrimeSetBits(self, left: int, right: int) -> int:
        count = 0
        for i in range(left, right + 1):
            c = 0
            n = bin(i).count("1")
            for j in range(1, n + 1):
                if n % j == 0:
                    c += 1
            if c == 2:
                count += 1
        return count


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    left = 6
    right = 10
    solution=Solution()
    print(solution.countPrimeSetBits(left,right))

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
