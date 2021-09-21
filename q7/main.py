# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.

class Solution:
    def reverse(self, x: int) -> int:
        if x<0:
            temp=-int(str(x)[1:][::-1])
            if (temp<-pow(2,31)) or (temp>pow(2,31)-1):
                return 0
            return temp
        else:
            temp=int(str(x)[::-1])
            if (temp<-pow(2,31)) or (temp>pow(2,31)-1):
                return 0
            return temp

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    solution=Solution()
    x=1534236469
    print(solution.reverse(x))

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
