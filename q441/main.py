# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.

class Solution:
    def arrangeCoins(self, n: int) -> int:
        l,r=0,n
        i=0
        while l<=r:
            i=i+1
            print(i)
            m=(l+r)//2
            cap=m*(m+1)//2
            if cap==n:
                return m
            if n<cap:
                r=m-1
            else:
                l=m+1
        return r


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    n=1804289383
    solution=Solution()
    print(solution.arrangeCoins(n))


# See PyCharm help at https://www.jetbrains.com/help/pycharm/
