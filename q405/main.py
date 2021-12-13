# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.


class Solution:
    def toHex(self,num:int)->str:
        if num==0:
            return "0"
        elif num<0:
            num=num+2**32
        res=""
        letter="0123456789abcdef"
        while num>0:
            res=letter[num%16]+res
            num//=16
        return res

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    solution=Solution()
    num = 26
    print(solution.toHex(num))

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
