# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.

class Solution:
    def canWinNim(self,n:int)->bool:
        return n%4!=0
    def canWinNim_slow(self, n: int) -> bool:
        if n<=3:
            return True
        if n==4:
            return False

        winning_case=[0]*(n+1)
        for i in range(4):
            winning_case[i]=1
        winning_case[4]=0
        for i in range(5,n+1):
            if ((winning_case[i-1]==1) and (winning_case[i-2]==1) and (winning_case[i-3]==1)):
                winning_case[i]=0
            else:
                winning_case[i]=1
        return winning_case[-1]==1


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    n=40
    solution=Solution()
    print(solution.canWinNim(n))

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
