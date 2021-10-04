# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.


class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        if n<=0:
            return False
        while n>1:
            if n%3==0:
                n=n//3
            else:
                return False
        return True

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    n=27
    solution=Solution()
    print(solution.isPowerOfThree(n))


# See PyCharm help at https://www.jetbrains.com/help/pycharm/
