# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.

class Solution:
    def climbStairs(self, n: int) -> int:
        results=[0]*(n+1)
        for i in range(1,n+1):
            if i==1:
                results[i]=1
            elif i==2:
                results[i]=2
            else:
                results[i]=results[i-1]+results[i-2]
        return results[-1]

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    solution=Solution()
    n=2
    print(solution.climbStairs(n))

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
