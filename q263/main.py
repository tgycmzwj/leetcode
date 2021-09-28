# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.


class Solution:
    def isUgly(self, n: int) -> bool:
        n=abs(n)
        if n==0:
            return False
        while n>5:
            if n%2==0:
                n=n//2
            elif n%3==0:
                n=n//3
            elif n%5==0:
                n=n//5
            else:
                return False
        return True


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    n=-2147483648
    solution=Solution()
    print(solution.isUgly(n))

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
