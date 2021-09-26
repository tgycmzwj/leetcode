# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.


class Solution(object):
    def rangeBitwiseAnd(self, m, n):
        difference = n - m
        mask = -1
        while difference:
            difference >>= 1
            mask <<= 1
        return mask & m & n


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    left = 3
    right = 4
    left = 1
    right = 2147483647
    solution=Solution()
    print(solution.rangeBitwiseAnd(left,right))

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
