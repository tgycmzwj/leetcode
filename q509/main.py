# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.


class Solution:
    def fib(self, n: int) -> int:
        results=[1,1]
        if n==0:
            return 0
        if n<=2:
            return 1
        for i in range(3,n+1):
            results.append(results[-1]+results[-2])
        return results[-1]

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    n=2
    solution=Solution()
    print(solution.fib(n))

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
