# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.

class Solution:
    def integerReplacement(self, n: int) -> int:
        if n==1:
            return 0
        if n%2==0:
            return self.integerReplacement(n//2)+1
        else:
            return min(self.integerReplacement(n+1),self.integerReplacement(n-1))+1


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    n=7912834
    solution=Solution()
    print(solution.integerReplacement(n))

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
