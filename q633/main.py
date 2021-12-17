# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.

class Solution:
    def __init__(self):
        self.cache={}
        for i in range(1,pow(2,16)):
            self.cache[i]=i**2
    def judgeSquareSum(self, c: int) -> bool:
        if c==0:
            return True
        for i in range(1,int(pow(c,0.5))+1):
            if int(pow(c-i**2,0.5))==pow(c-i**2,0.5):
                return True
        return False


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    c = 4
    solution=Solution()
    print(solution.judgeSquareSum(c))

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
