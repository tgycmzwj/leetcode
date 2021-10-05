# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.


class Solution:
    def check_sequence(self,num:str,i,j):
        num1=int(num[:i+1])
        num2=int(num[i+1:j+1])
        num=num[j+1:]
        while len(num)!=0:
            num3=num1+num2
            if str(num3)==num[:len(str(num3))]:
                num=num[len(str(num3)):]
                num1,num2=num2,num3
            else:
                return False
        return True


    def isAdditiveNumber(self, num: str) -> bool:
        if len(num)<3:
            return False
        for i in range(0,len(num)-2):
            for j in range(i+1,len(num)-1):
                if num[i+1]=='0' and j>i+1:
                    continue
                if self.check_sequence(num,i,j)==True:
                    if (len(num[:i+1])==1) or (len(num[:i+1])>1 and num[0]!='0'):
                        return True
        return False



# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    num="199100199"
    num="1123589"
    num='1203'
    num='1023'
    num='101'
    num='000'
    solution=Solution()
    print(solution.isAdditiveNumber(num))

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
