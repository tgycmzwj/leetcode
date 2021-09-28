# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.

class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        if n<=0:
            return False
        while n>1:
            residual=n%2
            if residual!=0:
                return False
            n=n/2
        return True

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    n=16
    #n=1
    n=5
    n=6
    n=4
    solution=Solution()
    print(solution.isPowerOfTwo(n))

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
