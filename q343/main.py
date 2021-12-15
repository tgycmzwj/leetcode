# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.


class Solution:
    def integerBreak(self, n: int) -> int:
        cur_max=1
        for part in range(2,n):
            mean,reminder=n//part,n%part
            results=pow(mean+1,reminder)*pow(mean,((n-(mean+1)*reminder)//mean))
            cur_max=max(cur_max,results)
        return cur_max

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    n=3
    solution=Solution()
    print(solution.integerBreak(n))

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
