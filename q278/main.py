# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.


class Solution(object):
    def firstBadVersion(self, n):
        r = n-1
        l = 0
        while(l<=r):
            mid = l + (r-l)//2
            if isBadVersion(mid)==False:
                l = mid+1
            else:
                r = mid-1
        return l

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    n = 5
    bad = 4
    solution=Solution()
    print(solution.firstBadVersion(n))

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
