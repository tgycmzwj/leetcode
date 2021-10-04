# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.

def guess(guess:int,pick:int)->bool:
    if guess==pick:
        return 0
    if guess>pick:
        return -1
    if guess<pick:
        return 1

class Solution:
    def guessNumber(self, n: int) -> int:
        left=1
        right=n
        while left<right:
            mid=(left+right)//2
            if guess(mid,pick)==0:
                return mid
            elif guess(mid,pick)==-1:
                right=mid-1
            else:
                left=mid+1
        return left


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    n=2
    pick=2
    solution=Solution()
    print(solution.guessNumber(n))

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
